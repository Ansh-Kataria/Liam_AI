# Liam : Personal AI Assistant
# Made By : Ansh Kataria
# Date started : 17 December, 2020

# ----------Import packages----------
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests
import pywhatkit
import pyautogui
import time
import instaloader

# This path is used to create chrome browser environment to open some websites
chrome_path = "C:/Program Files/Google//Chrome/Application/chrome.exe %s"

# Constructing a Text to speech TTS_Engine instance
TTS_Engine = pyttsx3.init('sapi5')

# Getting current value of property
System_voices = TTS_Engine.getProperty('voices')

# Adds a property value to set to the event queue
TTS_Engine.setProperty('voice', System_voices[0].id)


# ----------To Speak-----------
def speak(audio):
    """This Function convert the given string to audio and speak it out"""
    TTS_Engine.say(audio)
    TTS_Engine.runAndWait()


# ----------To Wish the user----------
def wish_me():
    """This Function wishes You According to time"""

    # check current hour
    current_hour = int(datetime.datetime.now().hour)
    cur_time = datetime.datetime.now().strftime("%H:%M")

    # If current time is between 6 A.M and 12 noon it will wish Good Morning
    if 6 <= current_hour <= 12:
        speak("Good Morning!, It's {} in the morning".format(cur_time))

    # If current time is between 12 noon to 6 P.M it will wish Good Afternoon
    elif 12 < current_hour <= 18:
        speak("Good Afternoon!, It's {} in the evening".format(cur_time))

    # If current time is between 6 P.M to 9 P.M it will wish Good Evening and tell time in the evening
    elif 18 < current_hour <= 21:
        speak("Good Evening!, It's {} in the evening".format(cur_time))

    # Any other time it will wish Good Evening and tell time in the night
    else:
        speak("Good Evening!, It's {} in the night".format(cur_time))

    # After Wishing It will Introduce itself
    speak("I am Liam, I am here as your personal assistant. "
          "Tell me, How can I help you?")


# ---------To take command from user----------
def take_command():
    """This function takes input from user and return string output """
    # Creating a Recognizer
    recognizer = sr.Recognizer()

    # Setting Up the microphone
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print("User said: {}".format(query))  # User query will be printed.

    except Exception:
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


# --------Functions to fetch news--------------
def news():
    """This function can be used to fetch news of all types."""
    main_url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=faaa162e0e7747c0bc1c99ce536f3aae"

    # fetching data in json format
    main_page = requests.get(main_url).json()

    # getting articles in string article
    articles = main_page["articles"]

    # Empty list to add articles
    articles_list = []

    # List of number for executing articles number-wise
    number = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    # Adding articles to our list
    for article in articles:
        articles_list.append(article["title"])

    # Telling news one by one, speaking as well as printing
    for i in range(len(number)):
        print("today's {} news is: {}".format(number[i], articles_list[i]))
        speak("today's {} news is: {}".format(number[i], articles_list[i]))


def news_tech():
    """This function can be used to fetch news related to technology only"""
    main_url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=faaa162e0e7747c0bc1c99ce536f3aae"

    # fetching data in json format
    tech_page = requests.get(main_url).json()

    # getting articles in string article
    articles = tech_page["articles"]

    # Empty list to add articles
    articles_list = []

    # List of number for executing articles number-wise
    number = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    # Adding articles to our list
    for article in articles:
        articles_list.append(article["title"])

    # Telling news one by one, speaking as well as printing
    for i in range(len(number)):
        print("today's {} news is: {}".format(number[i], articles_list[i]))
        speak("today's {} news is: {}".format(number[i], articles_list[i]))


def news_sports():
    """This function can be used to fetch news related to sports only."""
    main_url = "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=faaa162e0e7747c0bc1c99ce536f3aae"

    # fetching data in json format
    sports_page = requests.get(main_url).json()

    # getting articles in string article
    articles = sports_page["articles"]

    # Empty list to add articles
    articles_list = []

    # List of number for executing articles number-wise
    number = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    # Adding articles to our list
    for article in articles:
        articles_list.append(article["title"])

    # Telling news one by one, speaking as well as printing
    for i in range(len(number)):
        print("today's {} news is: {}".format(number[i], articles_list[i]))
        speak("today's {} news is: {}".format(number[i], articles_list[i]))


# Main
if __name__ == '__main__':

    # Wishing you at the start of program
    wish_me()

    # Endless loop to continuously ask command from user
    while True:

        # Taking command from user
        command = take_command().lower()

        # ---------Logic For different tasks---------

        # To interact with liam
        if 'hi liam' in command:
            speak("How are you sir?")

        elif 'am fine' in command:
            speak("That's Great!")

        # To search anything on wikipedia
        elif 'wikipedia' in command:
            speak("Searching Wikipedia, Sir, Please wait!")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            print(results)
            speak(results)

        # To open Youtube in chrome
        elif 'open youtube' in command:
            webbrowser.get(chrome_path).open("youtube.com")

        # To open Google in chrome
        elif 'open google' in command:
            speak("Sir, What should i search on google?")
            task = take_command().lower()
            tabUrl = "http://google.com/?#q="
            webbrowser.get(chrome_path).open("{}".format(tabUrl + task))

        # To play music on Youtube
        elif 'play music on youtube' in command:
            speak("Sir, What should I play?")
            task = take_command().lower()
            pywhatkit.playonyt(task)

        # To open Stackoverflow in chrome
        elif 'open stackoverflow' in command:
            webbrowser.get(chrome_path).open("stackoverflow.com")

        # To open Github in chrome
        elif 'open github' in command:
            webbrowser.get(chrome_path).open("github.com")

        # To open Notepad
        elif 'open notepad' in command:
            n_path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(n_path)

        # To close Notepad
        elif 'close notepad' in command:
            speak("closing notepad , Sir!")
            os.system("taskkill /f /im notepad.exe")

        # To open IDE
        elif 'Open IDE' in command:
            Ide_path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.4\\bin\\idea64.exe"
            os.startfile(Ide_path)

        # To open whatsapp web
        elif 'open whatsapp' in command:
            webbrowser.get(chrome_path).open("web.whatsapp.com")

        # To open cmd
        elif 'open command prompt' in command:
            os.system("start cmd")

        # To close cmd
        elif 'close command prompt' in command:
            speak("closing command prompt , Sir!")
            os.system("taskkill /f /im cmd.exe")

        # To check your IP address
        elif 'ip address' in command:
            ip = requests.get("https://api.ipify.org").text
            speak("Your IP address is {} ".format(ip))

        # To play music from the local computer
        elif 'play music' in command:
            music_dir = 'D:\\New_Folder'  # Use address of your directory where music is stored
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        # To check the time
        elif 'the time' in command:

            # converting current time into string
            curr_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, The time is {}".format(curr_time))

        # To get some news
        elif 'tell me some news' in command:
            speak("Sir , please wait , fetching news related to tech for you.")
            news()

        # To get news related to technology
        elif 'tell me some news related to tech' in command:
            speak("Sir , please wait , fetching news related to tech for you.")
            news_tech()

        # To get news related to sports
        elif 'tell me some news related to sports' in command:
            speak("Sir , please wait , fetching news related to sports for you.")
            news_sports()

        # To know your location
        elif 'where we are' in command:
            speak("Wait Sir, let me check.")
            try:
                ip = requests.get("https://api.ipify.org").text
                url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
                geo_data = requests.get(url).json()
                print(geo_data)
                city = geo_data['city']
                state = geo_data['region']
                country = geo_data['country']
                speak("Sir am not sure but we are in {} city in {} state which is located in {}".format(city, state, country))

            except Exception:
                speak("Sorry Sir, Due to network issue am unable to find where we are. ")
                pass

        # To search instagram profile by giving username
        elif 'search instagram profile' in command:
            speak("Sir please enter the username which you have to search")

            # Input the username to search
            username = input("Enter username here: ")

            # Opening the profile in chrome
            webbrowser.get(chrome_path).open("www.instagram.com/{}".format(username))

            time.sleep(5)

            speak("Sir would you like to download the profile pic of this account")

            # Infinite loop until getting right input
            while True:
                try:

                    # taking command to download profile pic or not
                    condition = take_command().lower()

                    if 'yes' in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(username, profile_pic_only=True)
                        speak("It's done Sir, The profile picture is saved to downloads , you can check it.")
                        break
                    else:
                        pass
                except Exception:
                    speak("Sorry sir, I didn't hear you . Please repeat sir.")

        # To take a screenshot
        elif 'take a screenshot' in command:
            speak("Sir, what should i name the file?")

            # Name of file as input to save the screenshot
            filename = take_command().lower()
            speak("Taking the screenshot, please wait sir.")

            time.sleep(3)

            # Taking screenshot
            screenshot = pyautogui.screenshot()

            # saving screenshot
            screenshot.save("{}.png".format(filename))

            speak("Done Sir, The Screenshot is saved to our main folder.")

        # To switch the current window
        elif 'switch the window' in command:

            # Keep the alt key down
            pyautogui.keyDown("alt")

            # Press the tab key
            pyautogui.press("tab")

            # Break of one second
            time.sleep(1)

            # pull the alt key up
            pyautogui.keyUp("alt")

        # To shut down the system
        elif 'shut down the system' in command:
            os.system("shutdown /s /t 5")

        # To restart the computer
        elif 'restart the system' in command:
            os.system("shutdown /r /t 1")

        # To Turn on the sleep mode
        elif 'sleep the system' in command:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # Good Bye
        elif 'you can sleep now' in command:
            speak("Have a good day Sir.")
            exit()
