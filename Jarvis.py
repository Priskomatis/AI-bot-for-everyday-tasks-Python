import pyjokes
import os
import pywhatkit
import webbrowser

import json
from docx import Document
from Weather import Weather
from AIRobot import AI
from randfacts import randfacts
from datetime import datetime


jarvis = AI()


def facts():
    fact = randfacts.get_fact()
    print(fact)
    jarvis.say(fact)


def cur_time():
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S")
    message = time_now
    jarvis.say(message)

#GET A JOKE CODE
def joke():
    funny = pyjokes.get_joke()
    print(funny)
    jarvis.say(funny)





def google(search):
    jarvis.say("Searching for "+search)
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new('https://google.com/search?q=' + search)


def reddit():
    jarvis.say("Opening reddit")
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new("https://reddit.com")

#def youtube(search):
#    jarvis.say("Opening youtube")
#    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new("https://youtube.com/search?q=" + search)

def youtube(search):

    jarvis.say("Opening youtube")
    pywhatkit.playonyt(search)


#Shopping list code


def weather():
    myWeather = Weather()
    forecast = myWeather.forecast
    print(forecast)
    jarvis.say(myWeather.forecast)


command = ""
jarvis.say("Hello Priskon")

while True and command != "goodbye":
    try:
        command = jarvis.listen()
        command = command.lower()
    except:
        print("Ops there was an error")
        command = ""

    #print("command was:" +command)

    if command == "tell me a joke":
        joke()
        command = ""

    if command in ['what is the weather like', ' give me the forecast', 'whats the weather', 'hows the weather']:
        weather()
        command = ""
    if command in ['random fact', ' tell me a fact', 'tell me something random', 'give me a fact']:
        facts()
        command = ""
    if command in ['good morning jarvis', 'hello jarvis']:
        now = datetime.now()
        hr = now.hour
        if hr <= 0 <= 12:
            message = "Morning"
        if hr >= 12 <=17:
            message = "Afternoon"
        if hr >=17 <=21:
            message = "Evening"
        if hr > 21:
            message = "Night"
        message = "Good" + message + "sir"
        jarvis.say(message)
        command = ""
    if command in ['Tell me the time', 'what time is it', 'jarvis what time is it']:
        cur_time()
        command = ""
    if command in ['open google', 'Open Google']:
        jarvis.say("What you want me to search sir?")
        message = jarvis.listen()

        google(message)
        command = ""

    if command in ['open reddit', 'Open Reddit']:
        reddit()
        command = ""

#    if command in ['open youtube', 'Open Youtube']:
#        jarvis.say("What you want me to search for sir?")
#        message = jarvis.listen()

#        youtube(message)

#        command = ""

    if command in ['open youtube', 'Open Youtube']:

        jarvis.say("What you want me to search for sir?")
        message = jarvis.listen(3)

        youtube(message)

        command = ""

jarvis.say("Goodbye Priskon.")