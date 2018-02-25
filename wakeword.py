import speech_recognition as sr
class wakeword:
    "the class whihc implememts the wake word similar the snow boy"
    def isWake():
   # Record Audio
        r = sr.Recognizer()
        r.dynamic_energy_threshold = True
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration = 1);
            print("Say something!")
            audio = r.listen(source)

   # Speech recognition using Google Speech Recognition
        data = ""
        try:
       # Uses the default API key
       # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            #data=r.recognize_sphinx(audio);
            #print("Sphinx thinks you said " + data)
        if data =="lamp":
            return True;
        return False;
