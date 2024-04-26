import RPi.GPIO as GPIO
from time import sleep

pinLED = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pinLED,GPIO.OUT,initial=GPIO.LOW)

while True:
    GPIO.output(pinLED, GPIO.HIGH)
    print("led on")
    sleep(1)
    
    GPIO.output(pinLED, GPIO.LOW)
    print("led off")
    sleep(1)