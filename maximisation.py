import RPi.GPIO as GPIO
import time

def lightUp(n,p):
    a=[21,20,16,12,7,8,25,24]
    GPIO.setup(a[n],GPIO.OUT)
    GPIO.output(a[n],1)
    time.sleep(p)
    GPIO.output(a[n],0)

def blink(n,k,p):
    a=[21,20,16,12,7,8,25,24]
    GPIO.setup(a[n],GPIO.OUT)
    for i in range(k):
        GPIO.output(a[n],1)
        time.sleep(p)
        GPIO.output(a[n],0)
        time.sleep(p)

def runningLight(k,p):
    a=[21,20,16,12,7,8,25,24]
    i=0
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a[i],1)
    time.sleep(p)
    while k>0:
        GPIO.output(a[i],0)
        if i==7:
            i=0
        else:
            i+=1
        GPIO.output(a[i],1)
        time.sleep(p)
        k-=1

def runningDark(k,p):
    a=[21,20,16,12,7,8,25,24]
    i=7
    GPIO.setup(a,GPIO.OUT)
    GPIO.output(a,1)
    GPIO.output(a[i],0)
    time.sleep(p)
    while k>0:
        GPIO.output(a[i],1)
        if i==0:
            i=7
        else:
            i-=1
        GPIO.output(a[i],0)
        time.sleep(p)
        k-=1

def decToBinList(n):
    a=[21,20,16,12,7,8,25,24]
    q=[0]*8
    z=128
    i=0
    while z!=0:
        q[i]=n//z
        n=n%z
        z=z//2
        i+=1
    return q

def lightNumber(n):
    a=[21,20,16,12,7,8,25,24]
    q=decToBinList(n)
    GPIO.setup(a,GPIO.OUT)
    for i in range(8):
        GPIO.output(a[i],q[i])
    time.sleep(1)

def runningPattern(n,d):
    q=decToBinList(n)
    lightNumber(n)
    while True:
        if d==1:
            z=q[7]
            for i in range(7):
                q[7-i]=q[6-i]
            q[0]=z
        else:
            z=q[0]
            for i in range(7):
                q[i]=q[i+1]
            q[7]=z
        p=0
        for i in range(8):
            p=p+q[7-i]*(2**i)
        lightNumber(p)

GPIO.setmode(GPIO.BCM)
#runningPattern(3,0)
GPIO.setup([21,20,16,12,7,8,25,24],GPIO.OUT)
GPIO.cleanup()