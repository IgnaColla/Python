import pyttsx3 #pip install pyttsx3 && sudo apt install espeak
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #Elijo la voz con el indice
newVoiceRate = 190 #Velocidad con la que habla
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Bienvenido nuevamente!")
    speak("Friday at your service.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recgnize_google(audio, language = "en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("MAIL@GMAIL.COM", "PASSWORD")
    server.sendmail("destination@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("PATH DONDE GUARDAR LA SCREEN - Usar \ ")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    
    while True:
        query = takeCommand().lower()
        print(query)
        
        if "time" in query:
            time()
        
        elif "date" in query:
            date()
        
        elif "offline" in query:
            quit()
        
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "PATH DE CHROME.EXE - Usar \ "
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        
        elif "logout" in query:
            os.system("shutdown - l")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        
        elif "play songs" in query:
            songs_dir = "PATH DE SONGS - Usar \ "
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        
        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())
        
        elif "screenshot" in query:
            screenshot()
            speak("Done")
        
        elif "cpu" in query:
            cpu()
        
        elif "joke" in query:
            jokes()