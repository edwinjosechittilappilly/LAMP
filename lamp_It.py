from main import main as m
class lamp_It:
    # # lamp main function with how and which all functions need to be called
    def lamp_it(data):
        answer="";
        if "how are you" in data:
            answer=str(m.lamp.get_response(data));
            print(answer);
            m.speak(answer);
 
        elif "what time is it" in data:
            m.speak(ctime())
        
        elif "name" in data:
            answer=str(m.lamp.get_response(data));
            m.speak(answer);
 
        elif "where is" in data:
            wikipedia.set_lang("en");
            answer=wikipedia.summary(ask,sentences =2);
            m.speak(answer);
        elif "can you hear me" in data:
            m.speak("yes i can hear you ");
        
        elif "search" in data:
            answer=online(data);
            m.speak(answer);
        elif "calculate" in data:
            answer=online(data);
            m.speak(answer);
        elif "math" in data:
            answer=online(data);
            m.speak(answer);
        else:
            answer=str(m.lamp.get_response(data));
            m.speak(answer);




