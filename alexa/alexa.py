import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from time import sleep

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 200)
command = ''


# speaker speech the sound taken from the microphone
def talk(text):
    engine.say(text)
    engine.runAndWait()


# taking command from microphone
def take_command():
    global listener, command
    try:
        with sr.Microphone() as source:  # using the default microphone to recognize the sound
            # listener.adjust_for_ambient_noise()
            listener.adjust_for_ambient_noise(source)
            listener.dynamic_energy_threshold = True
            print("listening...")
            audio = listener.listen(source, timeout=3)
            command = listener.recognize_google(audio, language='eng-in').lower()  # using of engilsh only
            print("you said" + command)
            # command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa", "")
                print(command)
    except sr.UnknownValueError:
        listener = sr.Recognizer()
    return command


# running the commands taken by microphone
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace("who is heck is", '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        print("I have a google program and i love elon musk and his companies space X and tesla")
        talk("I have a google program and i love elon musk and his companies space X and tesla")
    elif "are you in wifi" in command:
        print("No, for now i am using a service provider SAFARICOM")
        talk("No, for now i am using a service provider SAFARICOM")
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    else:
        talk("please try again in command option")
        sleep(2)


while True:
    run_alexa()
