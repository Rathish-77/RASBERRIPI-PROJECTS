import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
while(True):
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)

    n=int(input())
    match(n):
        case 1:
            GPIO.output(2,GPIO.HIGH)
        case 0:
            GPIO.output(2,GPIO.LOW)
        case 3:
        while(True):
            GPIO.output(2,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(2,GPIO.LOW)
            time.sleep(2)
            GPIO.output(3,GPIO.HIGH)
            time.sleep(2)
            GPIO.output(3,GPIO.LOW)
            time.sleep(2)
        case _:
            print("EXIT")
            break
        
        
        
