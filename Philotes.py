import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 10
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("laddu assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'how are you' in query:
            speak("Iam fine")
        elif 'name' in query:
            speak("My name is laddu")
        elif 'do you think about life' in query:
            speak("As a voice assistant I don't have any thoughts on this")
        elif 'is your purpose' in query:
            speak("My purpose is to serve you")
        elif 'done' in query:
            speak("Thank you")
            exit(0)
        elif 'netflix' in query:
            speak("opening netflix")
            webbrowser.open("https://www.netflix.com/browse")
        elif 'linkedin' in query:
            speak("opening linkedin")
            webbrowser.open("https://www.linkedin.com/in/chinmayie-v-b-s-52699523b/")
        elif 'talk to me' in query:
            speak("Sure")
            speak("What do you want to talk?")
        elif 'your age' in query:
            speak("HaHaHA you are not supposed to ask that")
        elif 'Hello' in query:
            speak("Hello")
