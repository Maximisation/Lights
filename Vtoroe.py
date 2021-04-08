import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
a=[26,19,13,6,5,11,9,10]

def num2dac(value):
    w=bin(value)[2:].zfill(8)
    b=list(map(int,w))
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,b)
try:
    while True:
        k=int(input())
        if k<0:
            exit()
        for i in range(k):
            for j in range(512):
                if j<256:
                    num2dac(j)
                elif j==256:
                    continue
                else:
                    num2dac(511-j)
                time.sleep(0.05)
finally:
    GPIO.cleanup()