import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import requests

# ------------------ SETUP ------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

WEATHER_API_KEY = "5d6d4e021d380cd835c1879a1ff54eff"
NEWS_API_KEY = "65727faa945248b8a46a2bf32e92ad07"

# ------------------ SPEAK ------------------
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

# ------------------ TAKE COMMAND ------------------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "none"

    return query.lower()

# ------------------ WEATHER FUNCTION ------------------
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    data = requests.get(url).json()

    if data["cod"] != 200:
        speak("City not found")
        return

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    speak(f"The temperature in {city} is {temp} degree Celsius with {desc}")

# ------------------ NEWS FUNCTION ------------------
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    data = requests.get(url).json()

    articles = data["articles"][:5]

    speak("Here are the top news headlines")
    for i, article in enumerate(articles, 1):
        speak(f"News {i}: {article['title']}")

# ------------------ MAIN ------------------
if __name__ == '__main__':
    speak("Philotes assistant activated")
    speak("How can I help you")

    while True:
        query = take_command()

        # -------- Wikipedia --------
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        # -------- Weather --------
        elif 'weather' in query:
            speak("Which city?")
            city = take_command()
            get_weather(city)

        # -------- News --------
        elif 'news' in query:
            get_news()

        # -------- Maps --------
        elif 'map' in query or 'location' in query:
            speak("What location?")
            location = take_command()
            webbrowser.open(f"https://www.google.com/maps/search/{location}")

        # -------- Spotify --------
        elif 'spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com")

        # -------- YouTube --------
        elif 'youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        # -------- Google --------
        elif 'google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        # -------- Basic Conversation --------
        elif 'how are you' in query:
            speak("I am fine, how can I assist you")

        elif 'your name' in query:
            speak("My name is Philotes")

        # -------- Exit --------
        elif 'done' in query or 'exit' in query:
            speak("Goodbye")
            break

        else:
            speak("Sorry, I am still learning this command")
