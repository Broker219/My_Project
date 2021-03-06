import random
import pyttsx3


def speak(what):
    print(what)
    speak_engine.setProperty('rate', 230)
    speak_engine.setProperty('volume', 0.9)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()
speak('Внимание, анекдот')
smile = [
    'Сын спрашивает у отца: - Посоветуй отец что лучше сделать - пойти в армию или жениться? '
    'Отец говорит: - Сынок если ты женишься то считай что пропало. '
    'А если пойдёшь в армию, то у тебя будет два путя - '
    'либо тебя убьют либо вернёшься живой. Если живой вернёшься то считай что пропало. А если убьют то '
    'у тебя будет два путя - похоронят тебя либо под сосёнкой либо под берёзкой. Если под берёзкой то считай, '
    'что пропало. А если под сосёнкой то у тебя два путя будет - пойдёшь ты либо на карандаши либо на бумагу. '
    'Если на карандаши то считай что пропало. А если на бумагу то у тебя два путя будет - либо на пищевую '
    'либо на туалетную. Если на пищевую то считай что пропало. А если на туалетную то у тебя будет два путя - '
    'попадёшь либо в мужской туалет либо в женский. Если в мужской то считай что пропало. А если в женский '
    'то у тебя будет два путя - будут тобой пользоваться либо спереди либо сзади. Если сзади то считай что пропало,'
    'А если спереди то считай что женился...',

    'Сегодня окончательно убедился что фразы "Чё это там ты жрёшь?" и "Чё это там у тебя?" заставляют собаку '
    'жевать в три раза быстрее.',
    
    '— Вот мне стало интересно куда за молоком ходила мама семерых козлят если она сама — коза? '
    '— Любой маме нужен аргумент чтобы иногда свалить из своего дома где сидят ее семеро детей.',
    
    'В ресторане официант подходит к столику: — Вы готовы сделать заказ? '
    'Напомню вам что дети сегодня у нас едят бесплатно.'
    '— А-а! Тогда мне и жене по стакану воды а ребенку три супа из акульих плавников,'
    'три салата с трюфелями три лобстера в чесночном соусе и бутылку Шато Де Талю 1969 года...'
        ]

smiles = random.choice(smile)
speak(smiles)
