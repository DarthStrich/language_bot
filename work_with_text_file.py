import gtts
import random
# import main

"""Читаем и выгружием пару в виде словаря"""


def read_dict():
    d = {}
    with open('dict_text.txt', 'r') as file:
        for line in file:
            key, *value = line.split()
            d[key] = value
        return d


"""Рандомно составляем список из пяти пар"""


def random_5(dict):
    d = {}
    for i in range(5):
        dict_l = dict
        # print(dict_l)
        rand = random.choice(list(dict_l))
        # print(rand)
        rand_doble = random.choice(dict_l[rand])
        # print(rand_doble)
        d[rand] = rand_doble
    return d


"""Записываем в файл по одной стоке"""


def write_dict(a, b):
    strii = ''
    # a = input('engl: ')
    # b = input('rus: ')
    strii = "\n" + a + ' ' + b
    strii = strii.lower()
    print(strii)
    file = open('dict_text.txt', 'a')
    file.write(strii)
    file.close()


"""Записываем создаём МП3 файл"""


def create_mp3(dict):
    str_l = dict
    file = open('from_file.mp3', 'ab')
    for a, b in str_l.items():
        b = str(b)
        tts1 = gtts.gTTS(text=a, lang='en')
        tts2 = gtts.gTTS(text=b, lang='ru')

        tts1.write_to_fp(file)
        tts2.write_to_fp(file)
    file.close()
    print('Записал')


