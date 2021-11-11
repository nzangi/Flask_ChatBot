import speech_recognition as sr
from time import ctime
import webbrowser
from time import sleep
import os
import playsound
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source, phrase_time_limit=2)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio).lower()
            # nzangi_speaks('How can I help you?')
        except sr.UnknownValueError:
            nzangi_speaks("Sorry, I did not get that")
        except sr.RequestError:
            nzangi_speaks("Sorry, my speech service is down")
        return voice_data


def nzangi_speaks(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    file = random.randint(1, 1000000)
    audio_file = 'audio-' + str(file) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        nzangi_speaks('your name is nzangi muoki')
    if 'what time is it' in voice_data:
        nzangi_speaks(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        sleep(1)
        nzangi_speaks('Here is what I found for' + search)
    if 'location' in voice_data:
        location = record_audio('What location do you want to search?')
        url = 'https://www.google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        sleep(1)
        nzangi_speaks('Here is what I found for' + location)
    if 'exit' in voice_data:
        nzangi_speaks('you are exiting the program, thank you. have a good day')
        exit()


sleep(1)

nzangi_speaks('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
