# Truy cập dữ liệu từ thư viện
import speech_recognition
import pyttsx3
from datetime import date, datetime
import wikipedia
import os
import playsound
import pyaudio
import webbrowser
import random
import requests, json  # Dùng để lấy data weather
from googletrans import Translator
from gtts import gTTS

# Khai báo biến
Lina_ear = speech_recognition.Recognizer()
Lina_mouth = pyttsx3.init()
Lina_brain = "Hello Sir, good day today!. Can I Help you"
print("Lina: " + Lina_brain)

Lina_mouth.say(Lina_brain)
Lina_mouth.runAndWait()

# Thay đổi giọng EN dùng cho câu trả lời tiếng anh
voices = Lina_mouth.getProperty('voices')
Lina_mouth.setProperty('voice', voices[0].id)  #0 for male
#meomeo_mouth.setProperty('voice', voices[1].id)   #1 for female

def sayvi(Lina_brain): # Lina Nói Tiếng Việt
	tv = gTTS(text = Lina_brain, lang = 'vi')
	gionggoogle = "sayvi.mp3"
	tv.save(gionggoogle)
	playsound.playsound(gionggoogle,True)
	os.remove(gionggoogle)

def sayen(Lina_brain): # Lina Nói Tiếng Anh
	ta = gTTS(text = Lina_brain, lang = 'en')
	gionggoogle = "sayen.mp3"
	ta.save(gionggoogle)
	playsound.playsound(gionggoogle,True)
	os.remove(gionggoogle)

def listen(): # Lina nghe
	with speech_recognition.Microphone() as mic:
		Lina_ear.adjust_for_ambient_noise(mic) # Giảm tiếng ồn cho mic
		print("Lina: I'm Listening")
		audio = Lina_ear.listen(mic)	 # or cách bên dưới
		# audio = Lina_ear.record(mic, duration=4) # Chỉ bậc mic trong 4 giây
	try:
		you = Lina_ear.recognize_google(audio)
	except:
		you = "..."
	print("You: " + you)
	return you

def translate(key):
	translator = Translator()
	trans = (translator.translate(key, src='en', dest='vi')).text
	return trans

def weather(city_name):
	# vào https://home.openweathermap.org/api_keys
	# tạo acc lấy API key free
	api_key = "2494be065c082e8c0f3bc4cc778af73a" 
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	response = requests.get(complete_url) 
	x = response.json() 
	if x["cod"] != "404": 
	    y = x["main"] 
	    current_temperature = int(y["temp"] - 273.15) # K = C + 273.15
	    current_pressure = y["pressure"] 
	    current_humidiy = y["humidity"] 
	    z = x["weather"] 
	    weather_description = z[0]["description"] 
	    weather_description = translate(weather_description)	# Dùng google dịch dữ liệu miêu tả
	    Lina_brain = "Hiện đang có " + str(weather_description) + ", Nhiệt độ là " + str(current_temperature) + " độ C, " + "Độ ẩm là " + str(current_humidiy) + "%"
	else: 
	    Lina_brain = "Không tìm thấy tên thành phố"
	return Lina_brain

# AI Lina
def Lina():
	while True:
		# Robot thảo luận
		you = listen()
		if you == "...":
			Lina_brain = "I'm listening"
		elif "Hello" in you or "Hi" in you or "Lina" in you :
			Lina_brain = "Hello Sir, Can I help you"
		elif "today" in you:
			today = date.today()
			Lina_brain = today.strftime("%d/%m/%Y")
		elif "I love you" in you:
			Lina_brain = "I love you, me to"
		elif "what's your name" in you or "your name" in you:
			Lina_brain = "I am Lina"
		elif "What is your date of birth" in you:
			Lina_brain = "I was born July 5, 2020"
		elif "time" in you:
			now = datetime.now()
			Lina_brain = now.strftime("%H hours %M minutes %S seconds")
		elif "weather" in you:
			Lina_brain = "Nói tên thành phố"
			you = listen()
			print("You search: " + you)
			Lina_brain = weather(you)
			if "Không tìm thấy tên thành phố" in Lina_brain:
				Lina_brain = "Hãy thử nhập: "
				you = input()
				Lina_brain = weather(you)
			print("Lina: " + Lina_brain)
		elif 'see you late' in you:
			Lina_brain = "Yes, Sir. You can call me if you want!"
				# Robot nói
			print("Lina: " + Lina_brain)
			Lina_mouth.say(lina_brain)
			Lina_mouth.runAndWait()
			break
		else:
			Lina_brain = "Sorry Sir, I understand. please again"

		# Robot nói
		print("Lina: " + Lina_brain)
		Lina_mouth.say(Lina_brain)
		Lina_mouth.runAndWait()
while True:
	you = listen()
	if "Hey, Lina" in you:
		Lina_brain = "Yes, Sir. I'am here"
	elif "goodbye" in you:
		Lina_brain = 'goodbye , sir'
		break


