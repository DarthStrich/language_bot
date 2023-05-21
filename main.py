import os
import sys
import time
import random

import work_with_text_file as wwt
import telebot
from telebot import types


answer_yes = ['+', 'да', 'д', 'Да', 'ага', 'угу', 'ye', 'yes', 'Y', 'go', 'Go', 'True', 'погнали',
              'Добавить пару в словарь', 'Тест. 5 слов']
bot = telebot.TeleBot('5617570560:AAF1QEqNPqMFr6_maPgrHSaURVKE7SfYA_M')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выгрузить МП3")
    btn2 = types.KeyboardButton('Добавить пару в словарь')
    btn3 = types.KeyboardButton('Тест. 5 слов')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Выберите чем займёмся", reply_markup=markup)


@bot.message_handler()
def get_text_messages(message):
    if message.text == 'Выгрузить МП3':

        dict_to_MP3 = wwt.read_dict()
        small_dict_to_MP3 = wwt.random_5(dict_to_MP3)
        wwt.create_mp3(small_dict_to_MP3)
        with open('from_file.mp3', 'rb') as mp3:
            bot.send_document(message.from_user.id, document=mp3)
    elif message.text == 'Добавить пару в словарь':
        input_words(message)
    elif message.text == 'Тест. 5 слов':
        test_func(message)


def input_words(message):
    if message.text in answer_yes:
        # if message.text == 'да' or message.text == 'д' or message.text == 'yes' or message.text == 'y' or message.text == '+' or message.text == 'Добавить пару в словарь':
        sent1 = bot.send_message(message.chat.id, 'Введите слово на английском')
        bot.register_next_step_handler(sent1, a_func)
        # print(sent1)
        # print(message.text, 'retgwerq')


def a_func(message):
    global a;
    a = message.text
    sent2 = bot.send_message(message.chat.id, f'Введите перевод слова {a}')
    bot.register_next_step_handler(sent2, b_func)
    # print(message.text)


def b_func(message):
    global b;
    b = message.text

    wwt.write_dict(a, b)
    sent3 = bot.send_message(message.chat.id, 'Продолжить ввод слов?')
    print(message.text, 'АЛО_1')

    bot.register_next_step_handler(sent3, input_words)
    print(message.text, 'АЛО_2')


def test_func(message):
    global qu_1, dict_to_MP3
    counter = 0
    if message.text in answer_yes:

        dict_to_MP3 = wwt.read_dict()
        qu_1 = random.choice(list(dict_to_MP3))
        an_1 = bot.send_message(message.chat.id, f'Как переводится {qu_1}?')
        bot.register_next_step_handler(an_1, test_2, counter)


def test_2(message, counter):
    print(message.text)
    answer = message.text
    answer = answer
    a = dict_to_MP3[qu_1]
    a = a[0]
    a = a
    if answer == a:
        print('Ура!')
        bot.send_message(message.chat.id, f'{answer} правильный ответ!')


    else:
        bot.send_message(message.chat.id, f'мб ошибка {a} правильный ответ!')
    an_2 = bot.send_message(message.chat.id, f'мб повторим?')
    bot.register_next_step_handler(an_2, test_func)

bot.polling()