import os
import sys
import time

import work_with_text_file as wwt
import telebot
from telebot import types

bot = telebot.TeleBot('5617570560:AAF1QEqNPqMFr6_maPgrHSaURVKE7SfYA_M')


# @bot.message_handler(commands=['start'])
# def star_mess(message):
#     bot.send_message(message.chat.id, 'Привет, пока у тебя 2 варианта: 1. Добавить пару в словарь 2. Получить аудио')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выгрузить МП3")
    btn2 = types.KeyboardButton('Добавить пару в словарь')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Выберите чем займёмся", reply_markup=markup)


@bot.message_handler()
def get_text_messages(message):
    if message.text == 'Выгрузить МП3':

        dict_to_MP3 = wwt.read_dict()
        wwt.create_mp3(dict_to_MP3)
        with open('from_file.mp3', 'rb') as mp3:
            bot.send_document(message.from_user.id, document=mp3)
    elif message.text == 'Добавить пару в словарь':
        input_words(message)
        # print(message.text)


def input_words(message):
    sent1 = bot.send_message(message.chat.id, 'Введите слово на английском')
    bot.register_next_step_handler(sent1, a_func)
    # print(sent1)
    print(message.text, 'retgwerq')


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
    bot.register_next_step_handler(sent3, question_words)
    print(message.text, 'АЛО')


def question_words(message):
    g = message.text
    print(message.text, 'АЛО2')
    if message.text == 'да' or message.text == 'д' or message.text == 'yes' or message.text == 'y' or message.text == '+':
        print(message.text, 'АЛО3')
        bot.register_next_step_handler(message, input_words)



bot.polling()
