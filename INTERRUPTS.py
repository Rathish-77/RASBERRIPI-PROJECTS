import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
BUTTON_PIN=16
GPIO.setup(2,GPIO.OUT)
def button_released_callback(channel):
    print("Button change in stage")
    

GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
'''GPIO.wait_for_edge(BUTTON_PIN,GPIO.RISING)
print("Button released")'''
GPIO.add_event_detect(BUTTON_PIN,GPIO.BOTH,callback=button_released_callback,
                      bouncetime=50)

while(1):
    
    GPIO.output(2,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(2,GPIO.LOW)
    time.sleep(2)
GPIO.output(2,GPIO.LOW)
