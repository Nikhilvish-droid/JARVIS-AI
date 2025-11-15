import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes 

def sptext():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        recogniser.adjust_for_ambient_noise(source)
        audio=recogniser.listen(source)
        try:
            print("recognising...")
            data=recogniser.recognize_google(audio)
            print(data)
        except:
            print(" not understand")

sptext()
