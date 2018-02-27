import RPi.GPIO as GPIO
import time
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
GPIO.setup(lights, GPIO.OUT, initial = 0);
    
def ret():
        file= open("mot.txt",'r')
        ff=file.readlines()
        file.close();
        va=ff[-1]
        var=str(va)
        print(var);
        if "1000" in var:
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)
            
            print("I am bending forward back")
            #GPIO.cleanup()
            time.sleep(3);
            return "I am bending forward back"
        if "0100" in var:
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            print("I am bending backward back")
            time.sleep(3);
            #GPIO.cleanup()
            return "I am bending backward back"
        if "0010" in var:
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)
            print("I am bending left back")
            time.sleep(3);
            #GPIO.cleanup()
            return "I am bending left back"
        if "0001" in var:
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)
            print("I am bending right back")
            time.sleep(3);
            #GPIO.cleanup()
            return "I am bending right back"
        return "turning"

class motion:
    "has functions related to the motion of the lamp"
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
    GPIO.setup(lights, GPIO.OUT, initial = 0)
    def mov(s):
        #general movement
        if s=="F" or s=="f":
            t=ret()
            print(t)
            file= open("mot.txt",'w')
            data="1000"
            file.write(data+"\n");
            file.close();
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending forward")
            #GPIO.cleanup()
            return "I am bending forward"
        if s=="B" or s=="b":
            t=ret()
            print(t)
            file= open("mot.txt",'w')
            data="0100"
            file.write(data+"\n");
            file.close();
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending backward")
            return "I am bending backward"
        if s=="l" or s=="L":
            t=ret()
            print(t)
            file= open("mot.txt",'w')
            data="0010"
            file.write(data+"\n");
            file.close();
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            print("I am bending left")
            return "I am bending left"
        if s=="R" or s=="r":
            t=ret()
            print(t)
            file= open("mot.txt",'w')
            data="0001"
            file.write(data+"\n");
            file.close();
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            print("I am bending Right")
            return "I am bending Right"
        if s=="t" or s=="T":
            t=ret()
            print(t)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
        
    def light(glow):
        if glow=="on":
            GPIO.output(126, GPIO.HIGH)
            print("Lights turned on")
            return "Lights turned on"
        if glow=="off":
            GPIO.output(126, GPIO.HIGH)
            print("Lights turned on")
            return "Lights turned on"
        
        



        
