import pyttsx3
import datetime
import random


def speak(what):
    print(what)
    speak_engine.setProperty('rate', 150)
    speak_engine.setProperty('volume', 0.9)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()
now = datetime.datetime.now().strftime('%H')

phrase = ['С возвращением сэр.',
          'Здраствуйте.',
          'Доброго времени суток.'
          ]
r_phrase = random.choice(phrase)
speak(r_phrase)






