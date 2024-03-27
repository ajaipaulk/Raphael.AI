import pyttsx3 #pip install pyttsx3 text to speech
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip
import psutil #pip
import pyjokes


engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time= datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

def greetings():
    speak("Welcome back Boss")
    time()
    date()
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning Sir")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir")
    elif hour>=16 and hour<22:
        speak("Good Evening Sir")
    else:
        speak("Goodnight Sir")

    speak("Raphael at your service. How may I help you")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1 #waits for 1 sec
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Say it Once more")
        return "None"
    return query 

def sendEmail(to,content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com","Password")
    server.sendmail("abc@gmail.com",to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("Screenshot.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery= psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__== "__main__":
    greetings()
    while True:
        query= takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I send?")
                content= takeCommand()
                to="receiver@gmail.com"
                sendEmail(to,content)
                print("Email has been sent!")
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath="c:/Program Files/Google/Chrome/Application/chrome.exe"
            search= takeCommand().lower()
            wb.get(chromepath).open_new_tab(search +".com")
        
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
 
        elif "play songs" in query:
            songs_dir="c:/This PC/Music"
            songs= os.listdir(songs_dir)#list of songs
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "remember that" in query:
            speak("What should I remember?")
            data=takeCommand()
            speak("You said me to remeber that" + data)
            remember =open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember =open("data.txt","r")
            speak("You said me to remember that"+remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")
        elif "cpu " in query:
            cpu()
        
        elif "joke" in query:
            jokes()

            
        elif "offline" in query:
            quit()
        



