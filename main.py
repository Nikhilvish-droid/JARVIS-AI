import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import pyjokes 

# converting users voice into text data.
def sptext():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        recogniser.adjust_for_ambient_noise(source)
        audio=recogniser.listen(source)
        try:
            print("recognising...")
            data=recogniser.recognize_google(audio)
            print(f"YOUR TEXT IS :{data.lower()}")
            return data.lower()
        except:
            textsp("sorry i cant hear you")

#converting text into computer/jarvis ai voice.
def textsp(data):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(data)
    engine.runAndWait()

if __name__=="__main__":
    ans="y"
    while ans=="y":
        data1=sptext()
        if data1=="hello":
            textsp("hello hello nikhil what can i help you.")

        elif "time" in str(data1):
            hour=time.strftime("%H")
            min=time.strftime("%M")
            textsp(f"oo,{hour} hour and {min}minutes.")

        elif "name" in str(data1) :
            textsp(" my my name is JARVIS AI. ")
            
        elif "old" in str(data1) :
            text="i am 25 years old."
            textsp(text)
        
        elif "youtube" in str(data1) :
            webbrowser.open("https://www.youtube.com/")

        elif "github" in str(data1) :
            webbrowser.open("https://github.com/Nikhilvish-droid")
        
        ans=input("enter y/n to activate JARVIS AI :")

    textsp("0  thank you ")   