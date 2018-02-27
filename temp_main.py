#from wakeword import wakeword as w
#while 1:
    #t=w.isWake();
    #print(t);

from features import motion as mot
from main import main as m
while 1:
    mot.reset()
    Q=str(input("Q:"))
    ans=mot.mov(Q);
    m.speak(ans);
    
