from pyowm import OWM
import pyttsx3


def speak(what):
    print(what)
    speak_engine.setProperty('rate', 230)
    speak_engine.setProperty('volume', 0.9)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()

owm = OWM('97c072f67effa46aaf77ea42789ce129')
mgr = owm.weather_manager().weather_at_place('minsk')
t = mgr.weather.temperature(unit='celsius')
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']

speak('Температура сейчас на улице ' + ('%.0f' % t1) + ' градуса по цельсию ')
speak('Ощущается как ' + ('%.0f' % t2) + ' градуса по цельсию ')
if ('%.0f' % t3) != ('%.0f' % t4):
    speak('Минимальная и максимальная температура сегодня, соответственно: ' + ' от ' +
          ('%.0f' % t4) + ' до ' + ('%.0f' % t3) + ' градусов по цельсию')
