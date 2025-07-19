#!/usr/bin/env
import speech_recognition as sr
import io
from subprocess import Popen, PIPE
from gtts import gTTS
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
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    proc =Popen(['mpg123', '-o', 'oss:/dev/dsp4', '--quiet', '-'], stdin=PIPE)
    proc.communicate(audio_buffer.read())


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
        Popen(answer_list[1].lower(), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    elif answer == 'quit':
        text_to_speech('OK I quit')
        exit()


while True:
    text = listen_for_command()
    if text is not None:
        if text in Triger_assistent:
            what_to_do()
