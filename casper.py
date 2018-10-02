#!/usr/bin/env
import speech_recognition as sr
from gtts import gTTS
import os
from subprocess import Popen
from getpass import getuser

username = getuser()
Triger_assistent = [
    'hey Casper',
    'eh Casper',
    'hey casper',
    'eh casper'
    'Hey Casper',
    'Eh Casper',
    'Hey casper',
    'Eh casper']


def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Something!')
        audio = r.listen(source)
        print('Done!')
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        pass
        return None
    else:
        print(text)
        return text


def text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    audio_file = 'temp.mp3'
    tts.save(audio_file)
    os.system(f'mpg123 {audio_file} --quiet')
    os.remove(audio_file)


def what_to_do():
    text_to_speech('What you whant to Do')
    while True:
        answer = listen_for_command()
        if answer is None:
            text_to_speech('I did not understand')
        else:
            break
    answer_list = answer.split()
    if answer_list[0] in ['open', 'Open']:
        text_to_speech(f'Opening {answer_list[1]}')
    elif answer == 'quit':
        text_to_speech('OK I quit')
        exit()


while True:
    text = listen_for_command()
    if text is not None:
        if text in Triger_assistent:
            what_to_do()
