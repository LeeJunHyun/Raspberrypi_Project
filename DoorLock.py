import RPi.GPIO as GPIO
import time

class OpenDoor():
    
    def __init__(self,GPIO,pin):


        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin,GPIO.OUT)
        self.p = GPIO.PWM(self.pin,50)
        self.p.start(0)

    def open(self):
        self.p.ChangeDutyCycle(1)
        time.sleep(0.5)
        self.p.ChangeDutyCycle(8)
        time.sleep(0.5)
        self.p.stop()

if __name__ =='__main__':
    opendoor = OpenDoor(GPIO,18)  
    opendoor.open()
