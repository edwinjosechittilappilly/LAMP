from lamp_It import lamp_It as l
from main import main as m
import os
class logger:
#m.speak("Hi Buddy , what can I do for you?")
    def ltrain(data,ans):
    #data = m.recordAudio();
    #data=str(input("Question:"));
    #ans=l.lamp_it(data);
    #m.speak(ans);
        file= open("train.txt",'a')
    # ask the user if the answer was satsfactory or not
    # if  not satisfactory ask for a new answer and then train again
##    choice=str(input("is the answer satisfactory ?y or n "))
##    if choice is "n":
##        ans=str(input("Enter the required response or answwer:"));
        file.write(data+"\n");
        file.write(ans+"\n");
        file.close();
        m.lamp.train([data,ans]);
    


