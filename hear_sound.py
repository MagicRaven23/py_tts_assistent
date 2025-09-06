import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class Hear:
    def __init__(self, name, r):
        self.name = name
        self.r = r    
    
    def voice(self):
        r = self.r
        with sr.Microphone() as source:
            print("Talk...")
            audio_text = r.listen(source)
            try:
                text = r.recognize_google(audio_text)
                print("You said:", text)
                return text.lower()   # damit Groß/Kleinschreibung egal ist
            except:
                print("Sorry, I did not get that")
                return ""             # falls nichts erkannt wurde

    def __str__(self):
        return f"{self.name}"


p1 = Hear("computer", sr.Recognizer())

while True:
    if p1.voice() == "computer":
        print("Hello")
        engine.say("yes")
        engine.runAndWait()
        engine.stop()
    else:
        print("Not recognized")
