import RPi.GPIO as GPIO
from time import sleep
pinLED1=5
pinLED2=13
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pinLED1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pinLED2,GPIO.OUT,initial=GPIO.LOW)
while True:
    GPIO.output(pinLED1,GPIO.HIGH)
    print("led on")
    sleep(1)
    GPIO.output(pinLED1,GPIO.LOW)
    print("led off")
    sleep(1)

    GPIO.output(pinLED2,GPIO.HIGH)
    print("led on")
    sleep(1)
    GPIO.output(pinLED2,GPIO.LOW)
    print("led off")
    sleep(1)
    
    GPIO.output(pinLED1,GPIO.LOW)
    print("led off")
    sleep(1)
