import time
import pyjokes as pyjokes
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  !")
    else:
        speak("Good Evening !")
    speak("I am jarvis .")

def cname():
    speak("Which city related data do you want?")
    city = str(takeCommand())
    speak("What do you want to search?")
    what = (takeCommand())

    url="https://www.justdial.com/"+city+"/"+what
    print(url)
    return city


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "human"
    return query


if _name_ == "_main_":
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    cname()
