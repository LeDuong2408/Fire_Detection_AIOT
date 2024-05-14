import RPi.GPIO as GPIO
import time

def turn_on(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT) 
    GPIO.output(pin, GPIO.HIGH)

def turn_off(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT) 
    GPIO.output(pin, GPIO.LOW)
