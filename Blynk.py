import BlynkLib
import RPi.GPIO as GPIO
#from BlynkTimer import BlynkTimer


# Hàm để bật máy bơm
def turn_on_pump(water_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(water_pin, GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(water_pin, GPIO.LOW)
    print("Máy bơm đã được bật.")

# Hàm để tắt máy bơm
def turn_off_pump():
    GPIO.cleanup()
    print("Máy bơm đã được tắt.")

def connect_to_blynk(BLYNK_AUTH_TOKEN):
    # Initialize Blynk
    blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

    @blynk.on("connected")
    def blynk_connected():
        print("Raspberry Pi Connected to New Blynk") 

    return blynk

def turn_off_pump_blynk(blynk, water_pin):
    blynk.virtual_write(0,1)
    turn_off_pump()

def turn_on_pump_blynk(blynk, water_pin):
    blynk.virtual_write(0,0)
    turn_on_pump(water_pin)

def waterpump_blynk(blynk, water_pin):
    # Led control through V0 virtual pin
    @blynk.on("V0")
    def v0_write_handler(value):
    #    global led_switch
        if int(value[0]) != 0:
            turn_off_pump_blynk(blynk, water_pin)
        else:
            turn_on_pump_blynk(blynk, water_pin)
BLYNK_AUTH_TOKEN = 'ABG-zB6-wlnrX7Vc1aA0J5ANFjD9v7uG'
water_pin = 17
blynk = connect_to_blynk(BLYNK_AUTH_TOKEN)         

#if __name__ == '__init__':
#   BLYNK_AUTH_TOKEN = 'ABG-zB6-wlnrX7Vc1aA0J5ANFjD9v7uG'
#   water_pin = 17
#   waterpump_blynk(BLYNK_AUTH_TOKEN, water_pin)
