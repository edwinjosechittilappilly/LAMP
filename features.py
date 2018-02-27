import RPi.GPIO as GPIO 

class motion:
    "has functions related to the motion of the lamp"
    GPIO.setmode(GPIO.BCM);
    f = 5
    b = 6
    l = 13
    r = 19
    GPIO.setup(f, GPIO.OUT, initial = 0)
    GPIO.setup(b, GPIO.OUT, initial = 0)
    GPIO.setup(l, GPIO.OUT, initial = 0)
    GPIO.setup(r, GPIO.OUT, initial = 0)
    GPIO.output(f, GPIO.LOW)
    GPIO.output(b, GPIO.LOW)
    GPIO.output(l, GPIO.LOW)
    GPIO.output(r, GPIO.LOW)
    def mov(s):
        if s=="F" or s=="f":
            GPIO.output(5, GPIO.HIGH)
            print("I am bending forward")
            #GPIO.cleanup()
            return "I am bending forward"
        if s=="B" or s=="b":
            GPIO.output(6, GPIO.HIGH)
            print("I am bending backward")
            return "I am bending backward"
        if s=="l" or s=="L":
            GPIO.output(13, GPIO.HIGH)
            print("I am bending left")
            return "I am bending left"
        if s=="R" or s=="r":
            GPIO.output(19, GPIO.HIGH)
            print("I am bending Right")
            return "I am bending Right"
        



        
