import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests

# Chrome path
chrome_path = "C:/Program Files/Google//Chrome/Application/chrome.exe %s"

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

        elif 'hi liam' in query:
            speak("How are you sir?")

        elif 'am fine' in query:
            speak("That's Great!")

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.get(chrome_path).open("github.com")

        elif 'open notepad' in query:
            n_path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(n_path)

        elif 'Open code' in query:
            code_path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.4\\bin\\idea64.exe"
            os.startfile(code_path)

        elif 'open whatsapp' in query:
            webbrowser.get(chrome_path).open("web.whatsapp.com")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'ip address' in query:
            ip = requests.get("https://api.ipify.org").text
            speak("Your IP address is {} ".format(ip))

        elif 'play music' in query:
            music_dir = 'D:\\New_Folder'  # Use address of your directory where music is stored
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        elif 'the time' in query:
            curr_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, The time is {}".format(curr_time))

        elif 'quit' in query:
            speak("Have a good day Sir.")
            exit()
