import speech_recognition as sr
from pyttsx3 import speak
import pywhatkit
import webbrowser
import datetime
import time
import requests
import pyjokes
from bs4 import BeautifulSoup

API_KEY = "ed90488c7c793f2a1a6e52a02fd51538"
base_url = "https://api.openweathermap.org/data/2.5/weather/"

listener = sr.Recognizer()


def get_sound():
    try:
        print('listening...')
        speak('listening...')

        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def codechef_ratings():
    usernames = ['siddu2355', 'sidhu4641',
                 'dhanush30', 'gkey_akhilsaik', 'hellfire2004']
    for username in usernames:
        html = requests.get(f"https://codechef.com/users/{username}").text
        soup = BeautifulSoup(html, 'lxml')
        name = soup.find('h1', class_='h2-style').text
        rating_div = soup.find('div', class_='rating-number')
        if rating_div is not None:
            rating = int(rating_div.text[0:4].replace(
                "?", "").replace("i", ''))
        else:
            rating = 0
        print(f'''[
        username: {username},
        name: {name},
        rating: {rating}
],''')


def open_yT(comman):
    song = comman.replace('play', '')
    speak('playing ' + song)
    print('playing ' + song)
    pywhatkit.playonyt(song)


def get_curtime():
    time = datetime.datetime.now().strftime('%I:%M %p')
    print('Current time is ' + time)
    speak('Current time is ' + time)


def google_command():
    print("what do you what to search")
    speak("what do you what to search")
    search_key = get_sound()
    print(f"Searching {search_key}")
    speak(f"Searching {search_key}")
    url = f"https://www.google.com/search?q={search_key}"
    webbrowser.get().open(url)


def location():
    print("which place you want to search")
    speak("which place you want to search")
    searchLo = get_sound()
    print(f"Searching {searchLo}")
    speak(f"Searching {searchLo}")
    url = f"https://www.google.com/maps?q={searchLo}"
    webbrowser.get().open(url)


def get_a_joke():
    jok = pyjokes.get_joke()
    print(jok)
    speak(jok)


def whatsapp_message():
    contacts = {
        "bro": "+919391198374",
        "pranav": "+919347349353",
        "player": "+917981215753",
        "grand player": "+918333931019",
    }
    time = datetime.datetime.now().strftime('%I:%M %p')
    min = int(time[3:5])
    hour = int(time[0:2])
    ap = time[6:8]
    if ap == "PM" and hour != 00 and hour != 12:
        hour += 12
        print("To whom you want to send message to: ")
        speak("To whom you want to send message to: ")
        name = get_sound()
        x = 0
        for i in contacts:
            if i == name:
                x = 1
                print(f"what is your message to {i}")
                speak(f"what is your message to {i}")
                messa = get_sound()
                print(f"your message to {i} is \'{messa}\'")
                pywhatkit.sendwhatmsg(contacts[i], messa, hour, min+2)
        if x == 0:
            print(f"{name} is not in your contacts. ")
            speak(f"{name} is not in your contacts. ")


def weather_report():
    print("weather report of which city you want to look at? ")
    speak("weather report of which city you want to look at? ")
    city = get_sound()
    print(f"please wait fetching the weather report of {city}")
    speak(f"please wait fetching the weather report of {city}")

    response = requests.get(f"{base_url}?appid={API_KEY}&q={city}")
    if response.status_code == 200:
        data = response.json()
        result = {
            'lon': data['coord']['lon'],
            'lat': data['coord']['lat'],
            'temp': round(data["main"]['temp'] - 273, 2),
            'wind_speed': data['wind']['speed'],
            'pressure': data["main"]['pressure'],
            'humidity': data["main"]['humidity'],
        }
        print(f"""city: {city}
longitude: {result['lon']}
latitude: {result['lat']}
'temperature: {result['temp']}""")
        speak(
            f"The current temperature in {city} is {str(result['temp'])} degrees centigrade.")
    elif response.status_code == 404:
        print(f"The city {city} does not Exist.")
        speak(f"The city {city} does not Exist.")


def run_code():
    cmd = get_sound()
    command = cmd.lower()
    print(cmd)
    if 'play' in command:
        open_yT(command)
    elif "name" in command:
        print("I am John.")
        speak("I am John.")
    elif "hello" in command:
        print("Hi There, how can i help you?")
        speak("Hi There, how can i help you?")
    elif 'time' in command:
        get_curtime()
    elif 'google' in command:
        google_command()
    elif 'locate' in command:
        location()
    elif 'joke' in command:
        get_a_joke()
    elif 'whatsapp' in command:
        whatsapp_message()
    elif "weather" in command:
        weather_report()
    elif "codechef" in command:
        codechef_ratings()
    elif 'exit' in command:
        return False
    else:
        speak('Please say the command again.')


print("Hello I'm John. Your personal Assistant.")
speak("Hello I'm John. Your personal Assistant.")


while True:
    time.sleep(1)
    if run_code() == False:
        break
    else:
        run_code()
