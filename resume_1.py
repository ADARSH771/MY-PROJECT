import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(" Very Good morning Adarsh!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon! Adarsh")

    else:
        speak("Good Evening! Adarsh ")
    speak("HELLO!. Adarsh I am your friend AI speaker please tell me how may i help you")


def takecommand():
    # it takes microphone input from the user and returs string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please....")
        return "none"
    return query


def sendEmail(do, contant):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # server.login('youremail@gmail.com','your-password')
    server.login('narvekaradarsh772@gmail.com', 'narvekaradarsh771@gmail.com')
    # server.sendmail('youremail@gmail.com',to,content)
    server.sendmail('narvekaradarsh772@gmail.com')
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        # logic for executing tasks based on query
        # wishme("adarsh is a good boys")
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak('OK SIR I OPENING GOOGLE')
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            speak('OK SIR I OPENING instagram')
            webbrowser.open("instagram.com")
        elif 'play music' in query:
            webbrowser.open("https://wynk.in/music/package/new-hindi-songs/bb_1404393019358")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")
        elif 'open powerpoint' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)
        elif 'how are you' in query:
            speak('I am great sir what about you')
        elif 'Ram' in query:
            speak('RAAAM RAAM, HARE RAAM')
        elif 'quit' in query:
            speak('THANKS YOU FOR USING JARVIS .THIS IS DONE BY ADARSH.B.NARVEKAR ')
            exit()
        elif 'email to mayur' in query:
            try:
                speak("what should i say ? ")
                content = takecommand()
                to = "narvekaradarsh772@gmail.com"  # jisko email send karna hai wo
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry adarsh i cant able this")