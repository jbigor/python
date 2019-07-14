import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
	print(words)
	os.system("say " + words)


talk("Привет,,,")

def command():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)

	try:
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		print("Вы сказали: " + zadanie)
	except sr.UnknownValueError:
		talk(" говорите ")
		zadanie = command()

	return zadanie

def makeSomething(zadanie):

	if 'открой сайт' in zadanie:
		talk("Уже открываю")
		url = 'http://ya.ru'
		webbrowser.open(url)
	elif 'ева открой сайт' in zadanie:
		talk("Подожди открываю")
		url = 'http://ya.ru'
		webbrowser.open(url)
	elif 'привет' in zadanie:
		talk("Привет, Игорь")
		sys.exc_info()

	elif 'стоп' in zadanie:
		talk("Пока, Игорь")
		sys.exit()
	elif 'как тебя зовут' in zadanie:
		talk("Игорь, меня зовут ева")
		sys.exc_info()
	elif 'сколько тебе лет' in zadanie:
		talk("я не знаю")
		sys.exc_info()
	elif 'java' in zadanie:
		talk("да Игорь")
		sys.exc_info()
	elif 'ева' in zadanie:
		talk("да Игорь")
		sys.exc_info()
	elif 'посмотри курс биткоина' in zadanie:
		talk("щас проверю")
		url2 = 'https://yobit.net/ru/trade/BTC/USD'
		webbrowser.open(url2)
	elif 'смотри курс биткоина' in zadanie:
		talk("открываю юбит")
		url3 = 'https://yobit.net/ru/trade/BTC/USD'
		webbrowser.open(url3)





while True:
	makeSomething(command())
