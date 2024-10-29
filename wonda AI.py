import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 17:
        speak("Good afternoon!")
    elif hour >= 17 and hour < 20:
        speak("Good evening!")
    else:
        speak("Good evening!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    # Implement your email sending logic here
    pass

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            break
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
            break
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            break
        elif 'play music' in query:
            music_file = 'C:\\Users\\ganes\\Downloads\\Havana(PagalNew.Com.Se).mp3'  # Path to your music file
            try:
                if os.path.isfile(music_file):
                    os.startfile(music_file)
                else:
                    speak("The specified music file does not exist.")
            except Exception as e:
                speak("An error occurred while trying to play the music.")
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            break
        elif 'open code' in query:
            codepath = "C:\\Users\\Ganesh Agrahari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            break
        elif 'email to vishul' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vishulagrahari@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                speak("Sorry sir, I am not able to send this email at this moment.")
            break
        elif 'stop' in query or 'exit' in query:
            speak("Goodbye!")
            break
