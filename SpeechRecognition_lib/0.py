# python==3.6
# pip install SpeechRecognition
# pip install pocketsphinx

import speech_recognition as sr
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio0.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("you said ---  " + r.recognize_sphinx(audio) + "---")
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("error; {0}".format(e))
