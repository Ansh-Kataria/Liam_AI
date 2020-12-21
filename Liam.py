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


def speak(audio):
    """This Function convert the given string to audio and speak it out"""
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    """This Function wishes You According to time"""
    hours = int(datetime.datetime.now().hour)
    if 6 <= hours <= 12:
        speak("Good Morning!")
    elif 12 < hours <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Liam. How may I help you Sir?")


def take_command():
    """This function takes input from user and return string output """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print("User said: {}".format(query))  # User query will be printed.

    except Exception:
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()

        # Logic For different tasks
        if 'wikipedia' in query:
            speak("Searching Wikipedia, Sir, Please wait!")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
            speak("Anything else Sir!")

        elif 'hi liam' in query:
            speak("How are you sir?")

        elif 'am fine' in query:
            speak("That's Great!")
            speak("Anything else Sir!")

        # elif 'open idle' in query:
        #     idle_path = "C:\Users\anshk\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9"
        #     os.startfile(idle_path)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Anything else Sir!")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Anything else Sir!")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Anything else Sir!")

        elif 'open github' in query:
            webbrowser.open("github.com")
            speak("Anything else Sir!")

        elif 'play music' in query:
            music_dir = 'D:\\New_Folder'  # Use address of your directory where music is stored
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))
            speak("Anything else Sir!")

        elif 'the time' in query:
            curr_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, The time is {}".format(curr_time))
            speak("Anything else Sir!")

        elif 'quit' in query:
            speak("Have a good day Sir.")
            exit()
