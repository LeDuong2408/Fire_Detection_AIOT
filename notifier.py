from twilio.rest import Client
from google.cloud import storage
from datetime import datetime
import os

def upload_to_gcs(file_path, file_name,blob_name):
    bucket_name = "firedetect"
    full_file_path = os.path.join(file_path, file_name)
    # Khởi tạo một client GCS
    client = storage.Client.from_service_account_json("/home/pi/Fire-and-Smoke-Detection-using-Raspberry-Pi/Raspi_codes/My-fire.json")

    # Chọn hoặc tạo một bucket trong GCS
    bucket = client.get_bucket(bucket_name)

    # Chọn đối tượng blob trong bucket
    blob = bucket.blob(blob_name)
    with open(full_file_path , 'rb') as f:
        blob.upload_from_file(f)
    #print(f"Tải tệp lên {bucket_name} thành công.")
def alert_send():
    account_sid = "AC8d3a872527f0f00c346ca3e504278e13"
    auth_token = "d63b06c6391854c0fac6908bea8711c7"

    twili_phone_number = '+15304195846'
    my_phone_number = '+84382510794'
    whatsapp_phone_number = '+14155238886'
    file_path = "/home/pi/Fire-and-Smoke-Detection-using-Raspberry-Pi/Raspi_codes/"
    file_name = 'fire.jpg'
    file_extension = os.path.splitext(file_name)[1]
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    blob_name = f'fire_{current_time}{file_extension}'
    print(file_extension)
    upload_to_gcs(file_path,file_name,blob_name)
    #Twilio
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Fire Alert!! Detected fire. Please check your Whats'App to recieve a video clip of the event, recorded from Raspi camera",
        from_=f'{twili_phone_number}',
        to=f'{my_phone_number}')
    message = client.messages.create(
                media_url=[f'https://storage.googleapis.com/firedetect/{blob_name}'],
                body=" ࿄ Fire Alert!!",
                from_=f'whatsapp:{whatsapp_phone_number}',
                to=f'whatsapp:{my_phone_number}'
         )
    
    print(message.sid)




