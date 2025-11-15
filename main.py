import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes 
import win32com.client as w
import time

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

def textsp(data):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(data)
    engine.runAndWait()

sptext()
textsp(" hello!, nikhil what a shit are you talking man .")