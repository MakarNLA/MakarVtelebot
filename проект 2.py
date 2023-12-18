import telebot
import webbrowser
from telebot import types
import random

bot=telebot.TeleBot('6764474380:AAFfFcbtQtzRk2YGspT5tcKIU-qAxsI36pQ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    btn1 = types.KeyboardButton ('Ссылка на блог')
    btn2 = types.KeyboardButton ('Тексты')
    btn3 = types.KeyboardButton ('Рандомный текст со sports')

    markup.add(btn1, btn2)
    markup.row(btn3)

    bot.send_message(message.chat.id, f'День добрый, {message.from_user.first_name}{message.from_user.last_name}!',reply_markup= markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Ссылка на блог':
            bot.send_message(message.chat.id,'https://www.sports.ru/tribuna/blogs/footballsputnik/')
        elif message.text == 'Тексты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
            btn2 = types.KeyboardButton('Элисс Бен-Сегир')
            btn3 = types.KeyboardButton('Кентен Мерлен')
            btn4 = types.KeyboardButton('Антониу Силва')
            btn5 = types.KeyboardButton('Мало Гюсто')
            btn6 = types.KeyboardButton('Джорджо Скальвини')
            btn7 = types.KeyboardButton('Дезире Дуэ')
            btn8 = types.KeyboardButton('Элье Ваи')
            btn9 = types.KeyboardButton('Арнау Мартинес')
            btn10 = types.KeyboardButton('Куадио Коне')
            btn11 = types.KeyboardButton('Кастелло Лукеба')
            btn12 = types.KeyboardButton('Дестини Удоджи')
            btn13 = types.KeyboardButton('Алекс Скотт')
            btn14 = types.KeyboardButton('Габриель Вейга')
            btn15 = types.KeyboardButton('Милош Керкез')
            btn16 = types.KeyboardButton('На главную')
            markup.row(btn2, btn3, btn4)
            markup.row(btn5, btn6, btn7)
            markup.row(btn8, btn9, btn10)
            markup.row(btn11, btn12, btn13)
            markup.row(btn14, btn15, btn16)

            bot.send_message(message.chat.id,'Тексты',reply_markup = markup)
        elif message.text == 'Элисс Бен-Сегир':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3120784.html')
        elif message.text == 'Кентен Мерлен':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3121563.html')
        elif message.text == 'Антониу Силва':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3121948.html')
        elif message.text == 'Мало Гюсто':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3123036.html')
        elif message.text == 'Джорджо Скальвини':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3123949.html')
        elif message.text == 'Дезире Дуэ':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3125699.html')
        elif message.text == 'Элье Ваи':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3126051.html')
        elif message.text == 'Арнау Мартинес':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3127113.html')
        elif message.text == 'Куадио Коне':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3128941.html')
        elif message.text == 'Кастелло Лукеба':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3130434.html')
        elif message.text == 'Дестини Удоджи':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3131610.html')
        elif message.text == 'Алекс Скотт':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3132325.html')
        elif message.text == 'Габриель Вейга':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3135640.html')
        elif message.text == 'Милош Керкез':
            bot.send_message(message.chat.id, 'https://www.sports.ru/tribuna/blogs/footballsputnik/3139036.html')
        elif message.text == 'На главную':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Ссылка на блог')
            btn2 = types.KeyboardButton('Тексты')
            btn3 = types.KeyboardButton('Рандомный текст со sports')
            markup.add(btn1, btn2)
            markup.row(btn3)
            bot.send_message(message.chat.id,'Главная', reply_markup= markup)
        elif message.text == 'Рандомный текст со sports':
            n = random.randint(1, 3210350)
            bot.send_message(message.chat.id, f'https://www.sports.ru/tribuna/blogs/advert/{n}.html#supertop')

bot.polling(none_stop=True)
