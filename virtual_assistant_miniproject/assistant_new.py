import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import datetime
from urllib.parse import quote

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        listener.pause_threshold = 1
        audio = listener.listen(source)

        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
        except:
            return ""

def run_assistant():
    command = take_command()

    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")

    elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'hey Siri' in command:
        query = command.replace("hey Siri", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={quote(query)}")
        else:
            speak("What do you want me to search?")

    elif 'stop' in command or 'exit' in command:
        speak("Okay bye, see you again!")
        exit()

    else:
        speak("Sorry, I didn't understand that. Try: time, notepad, google, youtube or say hey Siri to search.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    speak(f"Hey {name}, I am ready! Ask me anything...")
    while True:
        run_assistant()
