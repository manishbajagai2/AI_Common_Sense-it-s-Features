import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("   Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("   Good Afternoon")

    else:
        speak("Good Evening!")
        print("   Good Evening")

    speak("I am your Assistant.  Tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("  Catching_ur_lips. Please wait...\n")
        audio = r.listen(source)

    try:
        print("   Processing ur request...\n")
        query = r.recognize_google(audio, language='en-in')
        print("  User said:\n"+query)

    except Exception as e:
        # print(e)
        print("  Say that again please...\n")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()

    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")

            speak("Sir, the time is "+ strTime)
            print("the time is:")
            print(strTime)



        elif 'egg falls down' in query:
            speak('if the egg falls down, it breaks')
            print("if the egg falls down, it breaks \n")


        elif 'glass falls down' in query:
            speak('if the glass falls down, it breaks')
            print("if the glass falls down, it breaks \n")

        elif 'touch fire' in query:
            speak('if you touch fire, it burns')
            print("if you touch fire, it burns \n")

        elif 'stop breathing' in query:
            speak('if you stop breathing, you will die')
            print("if you stop breathing, you will die \n")


        elif 'turn on the bulb' in query:
            speak('if you turn on the bulb, it glows')
            print("if you turn on the bulb, it glows \n")
