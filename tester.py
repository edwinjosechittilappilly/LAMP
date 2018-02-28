 
from lamp_It import lamp_It as l
from main import main as m
from wakeword import wakeword as w
from trainer import logger as log 
 
m.speak("call me lamp to wake me up")
while 1:
    while (w.isWake()):
        m.speak("I am here");
        data = m.recordAudio();
        #data=str(input("Question:"));
        ans=l.lamp_it(data);
        print(ans);
        m.speak(ans);
        m.speak("train data?");
        data = m.recordAudio();
        if data =="train":
            log.ltrain(data,ans);





