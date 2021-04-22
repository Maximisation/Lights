import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
a=[26,19,13,6,5,11,9,10]
aa=[21,20,16,12,7,8,25,24]
def num2dac(value):
    w=bin(value)[2:].zfill(8)
    b=list(map(int,w))
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,b)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)
GPIO.setup(4,GPIO.IN)
try:
    while True:
        start=0
        end=255
        while end-start!=1:
            mid=(end+start)//2
            num2dac(mid)
            time.sleep(0.01)
            t=GPIO.input(4)
            if t==0:
                end=mid
            else:
                start=mid
        print(str(round(start/255*3.3,2))+'V')
        o=round(start//(255/8))
        l=[0]*(7-o)+[1]*(o+1)
        GPIO.setup(aa,GPIO.OUT)
        GPIO.output(aa,l)

finally:
    GPIO.cleanup()