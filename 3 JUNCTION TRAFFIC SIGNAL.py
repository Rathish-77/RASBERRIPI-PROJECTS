  import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.out)#p1 red
GPIO.setup(3,GPIO.out)#p1 yellow
GPIO.setup(4,GPIO.out)#p1 green

GPIO.setup(9,GPIO.out)#p2 red
GPIO.setup(10,GPIO.out)#p2 yellow
GPIO.setup(11,GPIO.out)#p2 green

GPIO.setup(23,GPIO.out)#p3 red
GPIO.setup(24,GPIO.out)#p3 yellow
GPIO.setup(25,GPIO.out)#p3 green

GPIO.output(10,GPIO.HIGH) #p2- yellow
time.sleep(2)
GPIO.output(10,GPIO.LOW) #green

GPIO.output(2,GPIO.LOW)
GPIO.output(3,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
GPIO.output(9,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
GPIO.output(11,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(25,GPIO.LOW)

while(1):
    GPIO.output(4,GPIO.LOW)
    GPIO.output(9,GPIO.LOW) 
    GPIO.output(11,GPIO.HIGH) #green
    GPIO.output(2,GPIO.HIGH) #red
    GPIO.output(23,GPIO.HIGH)
    
    time.sleep(8)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(24,GPIO.LOW) 
    
    GPIO.output(11,GPIO.LOW)
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH) 
    GPIO.output(23,GPIO.LOW)
    
    time.sleep(8)
    GPIO.output(3,GPIO.HIGH)
    time.sleep(2)
    
    GPIO.output(3,GPIO.LOW) 
    GPIO.output(25,GPIO.LOW)
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(4,GPIO.HIGH)
    GPIO.output(2,GPIO.LOW)
    
    time.sleep(8)
    GPIO.output(10,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(10,GPIO.LOW)
