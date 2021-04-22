import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
a=[26,19,13,6,5,11,9,10]

def num2dac(value):
    w=bin(value)[2:].zfill(8)
    b=list(map(int,w))
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,b)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)

try:
    while True:
        k=int(input("Enter value (-1 to exit) "))
        if k<0 or k>255:
            exit()
        print('='+str(round(k/255*3.3,2))+'V')
        num2dac(k)
finally:
    GPIO.cleanup()