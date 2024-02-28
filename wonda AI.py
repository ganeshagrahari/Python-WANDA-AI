import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
print(voices[1].id)

'''This commpand speaks '''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
'''this command wish me'''
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good moring!")
    elif hour >= 12 and hour<17:
        speak("good afternoon!")
    elif hour >= 17 and hour<20:
        speak("good evening!")
    else:
        speak("good evening!")    


'''this commant takes input voice and return string output.'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold =0.5 # check and do experiment on ctrl + click
        audio = r.listen(source)
    try:
        print("Reconizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e :
             print("Say that again please....")
             return "None"
    return query
           
'''this funtion sends an email'''
# def sendEmail(to, content):
    

if __name__  == "__main__":
    wishMe() 
    # while True:
    if 1:
     query  = takeCommand().lower() 
    # logic  for executing tasks based on query 
     if 'wikipedia' in query :
         speak ('Searching wikipedia....')
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences = 2) 
         speak("According to wikipedia")
         print(results)
         speak(results)
     elif 'open youtube' in query:
          webbrowser.open("youtube.com")
     elif 'open google' in query:
          webbrowser.open("google.com")
     elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")
     elif 'play music' in query:
         music_dir = '#'
         songs = os.listdir(music_dir)
         print(songs)
         os. startfile(os.path.join(music_dir,songs[0]))# you can use random module for random song
     elif 'the time' in query:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir the time is {strTime}")
     elif 'open code' in query:
         codepath = "C:\\Users\\Ganesh Agrahari\\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"     
         os.startfile(codepath)
    #  elif 'email to vishul' in query:
    #      try:
    #          speak("What should I say?")   
    #          content = takeCommand()
    #          to = "vishulagrahari@gmail.com" 
    #          sendEmail(to ,content)
    #          speak("Email has been sent.")  
    #      except Exception as e:
    #          speak("sorry sir, i am not able to send this email at this moument")     