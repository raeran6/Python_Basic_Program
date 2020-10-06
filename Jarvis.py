import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')

engine.setProperty('rate',150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir ")
    elif hour>12 and hour<16:
        speak("Good afternoon sir ")
    elif hour>16 and hour<19:
        speak("Good Evening sir ")
    else:
        speak("Good Night sir ")
    speak("   i am jarvis how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say That again please....")
        return "None"
    return query




if __name__ == '__main__':
     wishMe()
     while True:
         query = takeCommand().lower()
         # logic
         if 'wikipedia' in query:
             speak("searching wikipedia...")
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query,sentences=3)
             speak("According to wikipedia")
             print(results)
             speak(results)
         elif 'open youtube' in query:
             speak("opening youtube, sir please wait")
             webbrowser.open("youtube.com")

         elif 'open google' in query:
             speak("opening  google ,sir please wait")
             webbrowser.open("google.com")

         elif 'open facebook' in query:
             speak("opening  facebook, sir please wait")
             webbrowser.open("facebook.com")

         elif 'open stack overflow' in query:
             speak("opening  stackoverflow , sir please wait")
             webbrowser.open("stackoverflow.com")


         elif 'play music' in query:
             speak("Playing Music Sir")
             music_dir ='C:\\Songs'
             songs = os.listdir(music_dir)
             r = random.randint(1,1500)
             os.startfile(os.path.join(music_dir,songs[r]))

         elif 'exit'in query:
             speak("Exiting sir ,  thankyou for your time")
             exit()









