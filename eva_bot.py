# начало разработки искуственного ителекта в linux

import speech_recognition as sr
import pyttsx3
import os
import sys
import webbrowser
import pyaudio

def output(x):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    print("Pc: "+x+".")
    engine.say(x)
    engine.runAndWait()
output("Hello, how are you")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say")
        r.pause_threshold = 1
        r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("Вы сказали:" + command)
    except sr.UnknownValueError:
       output("Error")
        zadanie = command()

    return zadanie
def makeSomething(zadanie):
    if 'open website' in zadanie:
        output("Open Web site")
        url = 'http://ya.ru'
        webbrowser.open(url)
    elif 'stop' in zadanie:

        sys.exit()
    while True:
        makeSomething(command())


