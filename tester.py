 
from lamp_It import lamp_It as l
from main import main as m
 
m.speak("Hi Buddy , what can I do for you?")
while 1:
    data = m.recordAudio();
    #data=str(input("Question:"));
    ans=l.lamp_it(data);
    m.speak(ans);





