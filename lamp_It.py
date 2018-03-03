from main import main as m
from features import motion as mot
import time
class lamp_It:
    # # lamp main function with how and which all functions need to be called
    def lamp_it(data):
        answer="";
        if "how are you" in data:
            answer=str(m.lamp.get_response(data));
            print(answer);
            return answer;
            
 
        elif "time" in data:
            answer=time.ctime();
            return answer;
            m.speak(ctime())
        
        elif " your name" in data:
            answer=str(m.lamp.get_response(data));
            return answer;
            
 
        elif "where is" in data:
            wikipedia.set_lang("en");
            answer=wikipedia.summary(ask,sentences =2);
            return answer;
            
        elif "can you hear me" in data:
            answer="yes i can hear you";
            return answer;
            m.speak("yes i can hear you ");
        
        elif "search" in data:
            data=data.replace("search","")
            data=data.replace("for"," ")
            answer=m.online(data);
            return answer;
        elif "what is" in data:
            data=data.replace("what","")
            data=data.replace("is"," ")
            answer=m.online(data);
            return answer;
             
        #elif "who is " in data:
            #answer=m.online(data);
            #return answer;
             
        elif "calculate" in data:
            data=data.replace("calculate","")
            answer=m.online(data);
            return answer;
             
        elif "math" in data:
            answer=m.online(data);
            return answer;
        elif "bend" in data:
            data=data.replace("bend","")
            if "front"in data or "forward" in data :
                s=mot.mov("f")
            elif "back" in data:
                s=mot.mov("b");
            elif "left" in data:
                s=mot.mov("l");
            elif "right" in data:
                s=mot.mov("r");
            else:
                s=mot.mov("t");
            return s;
        elif "turn on lamp" in data:
                s=mot.light("on");
                return s;
        elif "turn off lamp" in data:
                s=mot.light("off");
                return s;            
        else:
            answer=str(m.lamp.get_response(data));
            return answer;
             




