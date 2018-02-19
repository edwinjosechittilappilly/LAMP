from main import main as m
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
        
        elif "name" in data:
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
            answer=m.online(data);
            return answer;
             
        elif "who is " in data:
            answer=m.online(data);
            return answer;
             
        elif "calculate" in data:
            answer=m.online(data);
            return answer;
             
        elif "math" in data:
            answer=m.online(data);
            return answer;
             
        else:
            answer=str(m.lamp.get_response(data));
            return answer;
             




