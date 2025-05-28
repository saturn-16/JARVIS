import os
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from gtts import gTTS
import pygame
from dotenv import load_dotenv

# Load API keys securely
load_dotenv()
OPENAI_API_KEY = os.getenv("AIzaSyA9QJUpgs9gGVXubwUDBTRnf9j3ILlhEYk")
NEWSAPI_KEY = os.getenv("c7d507628f2440a0bf93c10acbf47b87")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def aiProcess(command):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful virtual assistant."},
                {"role": "user", "content": command}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI error: {e}")
        return "Sorry, I couldn't process that."


def processCommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "news" in command:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWSAPI_KEY}")
            if r.status_code == 200:
                articles = r.json().get('articles', [])
                for article in articles[:5]:
                    speak(article.get('title', 'No title'))
        except Exception as e:
            speak("Sorry, I couldn't fetch the news.")
            print(f"News fetch error: {e}")
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
    elif "stop" in command or "exit" in command:
        speak("Shutting down. Goodbye!")
        exit()
    else:
        output = aiProcess(command)
        speak(output)
import subprocess
import platform

# Dictionary of app names and their paths (edit based on your system)
APP_PATHS = {
    "chrome": r"C:\Users\Gaurav Kumar\Desktop\Gaurav",
    "notepad": r"C:\Windows",
    "vscode": r"C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "calculator": "calc",  
}

def open_app(app_name):
    try:
        app = APP_PATHS.get(app_name.lower())
        if app:
            if platform.system() == "Windows":
                if app.endswith(".exe"):
                    os.startfile(app)
                else:
                    subprocess.Popen(app, shell=True)
            else:
                subprocess.Popen([app])
            speak(f"Opening {app_name}")
        else:
            speak(f"I don't know how to open {app_name}")
    except Exception as e:
        speak(f"Sorry, I couldn't open {app_name}")
        print(f"App launch error: {e}")


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            print("Listening for wake word 'Jarvis'...")

            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                trigger = recognizer.recognize_google(audio).lower()

                if "jarvis" in trigger:
                    speak("Yes how may i help you gaurav?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)

        except Exception as e:
            print(f"Listening error: {e}")
