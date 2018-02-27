import RPi.GPIO as GPIO
import time

class motion:
    "has functions related to the motion of the lamp"
    def mov(s):
        GPIO.setmode(GPIO.BCM);
        f = 5
        b = 6
        l = 13
        r = 19
        lights = 26
        GPIO.setup(f, GPIO.OUT, initial = 0)
        GPIO.setup(b, GPIO.OUT, initial = 0)
        GPIO.setup(l, GPIO.OUT, initial = 0)
        GPIO.setup(r, GPIO.OUT, initial = 0)
        GPIO.setup(lights, GPIO.OUT,initial = 0)
        #general movement
        if s=="F" or s=="f":
            #ret()
            file= open("mot.txt",'w')
            data="1000"
            file.write(data+"\n");
            file.close();
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending forward")
            time.sleep(3)
            GPIO.cleanup()
            return "I am bending forward"
        if s=="B" or s=="b":
            #ret()
            file= open("mot.txt",'w')
            data="0100"
            file.write(data+"\n");
            file.close();
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending backward")
            time.sleep(3)
            GPIO.cleanup()
            return "I am bending backward"
        if s=="l" or s=="L":
            #ret()
            file= open("mot.txt",'w')
            data="0010"
            file.write(data+"\n");
            file.close();
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending left")
            time.sleep(3)
            GPIO.cleanup()
            return "I am bending left"
        if s=="R" or s=="r":
            #ret()
            file= open("mot.txt",'w')
            data="0001"
            file.write(data+"\n");
            file.close();
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            print("I am bending Right")
            time.sleep(3)
            GPIO.cleanup()
            return "I am bending Right"
        if s=="t" or s=="T":
            #ret()
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
            time.sleep(3)
            GPIO.cleanup()
            return "testing"
    def light(glow):
        GPIO.setmode(GPIO.BCM);
        f = 5
        b = 6
        l = 13
        r = 19
        lights = 26
        GPIO.setup(f, GPIO.OUT, initial = 0)
        GPIO.setup(b, GPIO.OUT, initial = 0)
        GPIO.setup(l, GPIO.OUT, initial = 0)
        GPIO.setup(r, GPIO.OUT, initial = 0)
        GPIO.setup(lights, GPIO.OUT,initial = 0)
        if glow=="on":
            GPIO.output(126, GPIO.HIGH)
            print("Lights turned on")
            GPIO.cleanup()
            return "Lights turned on"
        if glow=="off":
            GPIO.output(126, GPIO.HIGH)
            print("Lights turned on")
            GPIO.cleanup()
            return "Lights turned on"
        
        



        
