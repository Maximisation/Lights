import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
a=[26,19,13,6,5,11,9,10]

def num2dac(value):
    w=bin(value)[2:].zfill(8)
    b=list(map(int,w))
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,b)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)
GPIO.setup(4,GPIO.IN)
try:
    g=-1
    while True:
        j=0
        p=False
        for i in range(255):
            num2dac(i)
            time.sleep(0.01)
            t=GPIO.input(4)
            if t==0:
                p=True
                j=i-1
                break
        if g!=j and j>0 and p:
            print(str(round(j/255*3.3,2))+'V')
            num2dac(j)
            g=j
            time.sleep(0.1)
finally:
    GPIO.cleanup()