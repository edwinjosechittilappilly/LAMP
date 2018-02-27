import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
A = 5
B = 6
C = 13
D = 19
lights = 26
GPIO.setup(A, GPIO.OUT, initial = 0)
GPIO.setup(B, GPIO.OUT, initial = 0)
GPIO.setup(C, GPIO.OUT, initial = 0)
GPIO.setup(D, GPIO.OUT, initial = 0)
GPIO.setup(lights, GPIO.OUT,initial = 0)
GPIO.output(5, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)

class motion:
    "has functions related to the motion of the lamp"
    def reset():
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)

    
    def mov(s):
        GPIO.setmode(GPIO.BCM)
        A = 5
        B = 6
        C = 13
        D = 19
        lights = 26
        GPIO.setup(A, GPIO.OUT, initial = 0)
        GPIO.setup(B, GPIO.OUT, initial = 0)
        GPIO.setup(C, GPIO.OUT, initial = 0)
        GPIO.setup(D, GPIO.OUT, initial = 0)
        GPIO.setup(lights, GPIO.OUT,initial = 0)
        #general movement
        if s=="F" or s=="f":
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending forward")
            time.sleep(3)
            return "I am bending forward"
        if s=="B" or s=="b":
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending backward")
            time.sleep(3)
            return "I am bending backward"
        if s=="l" or s=="L":
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending left")
            time.sleep(3)
            return "I am bending left"
        if s=="R" or s=="r":
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            print("I am bending Right")
            time.sleep(3)
            return "I am bending Right"
        if s=="t" or s=="T":
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.LOw)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            time.sleep(3)
            return "testing"
    def light(glow):
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
        
        



        
