import speech_recognition
import time
import pyttsx3
import datetime
import os
from fuzzywuzzy import fuzz
from pyowm import OWM
import random
import webbrowser
from wikipediaapi import Wikipedia


option = {
    'name': ('окси', 'oxy', 'oksi', 'okci', 'окс', 'охи', 'фокси'),
    'tellbar': ('скажи', 'расскажи', 'подскажи', 'сколько', 'какая', 'какой', 'какие', 'который',
                'сейчас', 'включи', 'воспроизведи', 'найди', 'открой', 'покажи', 'поиграем',),
    'cmd': {'hello': ('привет', 'здравствуй', 'здорова', 'хай', 'добрый день', 'доброе утро', 'добрый вечер'),
            'q_time': ('время', 'час', 'сейчас время', 'сейчас час'),
            'q_date': ('сегодня день', 'сегодня число', 'день', 'месяц', 'год',
                       'сейчас год', 'сейчас месяц', 'дата'),
            'radio': ('музыку', 'радио', 'я проснулся'),
            'temperature': ('погода на улице', 'на улице холодно', 'на улице тепло', 'мне сегодня одеться',
                            'погода', 'холодно на улице', 'тепло на улице'),
            'smile': ('анекдот', 'порадуй меня', 'рассмеши меня'),
            'flatly': ('мне скучно', 'как-то мне скучно', 'здесь очень тихо', 'как-то здесь тихо'),
            'wikipedia': ('определение', 'значение', 'в гугл'),
            'videoyoutube': ('видео', 'видос'),
            'randint': ('случайное число', 'загадай число', 'выбери число')}
}


# Функции
def speak(what):
    print(what)
    speak_engine.setProperty('rate', 230)
    speak_engine.setProperty('volume', 0.9)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()


# отделение имени и вопросительного слова от команд
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print('--- Вы сказали: ' + voice)
        if voice.startswith(option['name']):
            cmd = voice

            for i in option['name']:
                cmd = cmd.replace(i, '').strip()
            for i in option['tellbar']:
                cmd = cmd.replace(i, '').strip()

            cmd = recognize_cmd(cmd)
            exe_cmd(cmd['cmd'])

    except speech_recognition.UnknownValueError:
        print('Голос не распознан!')
        return
    except speech_recognition.RequestError:
        print('Потеряно интернет соединение.')
    except KeyboardInterrupt:
        print('Программа завершена пользователем')


# распознование невнятной речи или отделение шума от речи
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in option['cmd'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC


# команды
def exe_cmd(cmd):
    try:
        if cmd == 'hello':
            os.system('python \\Voiceshelper\\modules\\hello.py')

        elif cmd == 'q_time':
            os.system('python \\Voiceshelper\\modules\\q_time.py')

        elif cmd == 'q_date':
            os.system('python \\Voiceshelper\\modules\\q_date.py')

        elif cmd == 'radio':
            os.system('python \\Voiceshelper\\modules\\radio\\radio_on_off.py')

        elif cmd == 'temperature':
            os.system('python \\Voiceshelper\\modules\\temp.py')

        elif cmd == 'smile':
            os.system('python \\Voiceshelper\\modules\\smile.py')

        elif cmd == 'flatly':
            choi = ["'python \\Voiceshelper\\modules\\radio\\radio_on_off.py'",
                    "'python \\Voiceshelper\\modules\\smile.py'"]
            choice = random.choice(choi)
            os.system(choice)

        elif cmd == 'wikipedia':
            for i in cmd['wikipedia']:
                cmd = cmd.replace(i, '').strip()
                speak('Нашла! Вывожу на экран')
                url = 'https://ru.wikipedia.org/wiki/' + cmd
                webbrowser.get().open(url)
                results = Wikipedia.summary
                speak('В википедии об этом говорится вот что: ' + results)

        elif cmd == 'videoyoutube':
            for i in cmd['videoyoutube']:
                cmd = cmd.replace(i, '').strip()
                speak('Открываю видео')
                url = 'https://www.youtube.com/results?search_query=' + cmd
                webbrowser.get().open(url)

        elif cmd == 'randint':
            speak('Укажите лимит чисел: ')
            voice1 = recognizers.recognize_google(language="ru-RU").lower()
            random_int = random.randint(1, voice1)
            speak(f' Ваше число {random_int}')

        else:
            print('Команда не распознана!')

    except KeyboardInterrupt:
        speak('Завершение программы')


# Приветстивие
now = datetime.datetime.now().strftime('%H')
owm = OWM('97c072f67effa46aaf77ea42789ce129')
mgr = owm.weather_manager().weather_at_place('minsk')
t = mgr.weather.temperature('celsius')
t1 = t['temp']

if 6 <= int(now) <= 12:
    speak('Доброе утро. Сейчас ' + datetime.datetime.now().strftime('%H:%M'))

elif 12 <= int(now) <= 17:
    speak('Добрый день. Сейчас ' + datetime.datetime.now().strftime('%H:%M'))

elif 18 <= int(now) <= 23:
    speak('Добрый вечер. Сейчас ' + datetime.datetime.now().strftime('%H:%M'))

else:
    speak('Странно, что вы ещё не спите. На часах ' + datetime.datetime.now().strftime('%H:%M'))

speak('Для того чтобы ко мне обратиться необходимо сказать мое имя, '
      'и далее указать функцию которую мне необходимо выполнить,'
      'Мое имя Окси.')
speak('Я могу выполнять следующие функции: \n'
      'Ответить время и дату, \n'
      'Рассказать метеосводку, \n'
      'Включить музыку, \n'
      'Рассказать анекдот, \n'
      'Найти и открыть в браузере определение слова, \n'
      'Открыть видео на платформе YouTube, \n'
      'Помочь загадать случайное число, ')
speak('Чем я могу вам служить?')
# Приветстивие

recognizers = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone(device_index=1)


with microphone:
    recognizers.adjust_for_ambient_noise(microphone, duration=2)

stop_listening = recognizers.listen_in_background(microphone, callback)
while True:
    time.sleep(0.1)
