import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
a=[26,19,13,6,5,11,9,10]

def decToBinList(n):
    q=[0]*8
    z=128
    i=0
    while z!=0:
        q[i]=n//z
        n=n%z
        z=z//2
        i+=1
    return q

def num2dac(value):
    w=decToBinList(value)
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,w)

try:
    while True:
        k=int(input())
        if k>255 or k<0:
            exit()
        num2dac(k) 
finally:
    GPIO.cleanup()