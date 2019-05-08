# начало разработки искуственного ителекта в linux
# думаю в будущем она будет говорить и заражать все компьютеры

import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
    print(words)
    os.system("say" + words)

talk("Привет, я ева")
