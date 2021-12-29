import telebot
from telebot import types
import datetime as dt

token = "5076480755:AAEpDGo_Q0qaPFwASzAf8n7KSARFQChHKCM"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '''Я умею...давать информацию о МТУСИ
    /arthas - ютуб канал
    /yandex - ссылка на яндекс
    /github - мой гитхаб
    также мошешь написать привет, кто ты, забей''')


@bot.message_handler(commands=['github'])
def github(message):
    bot.send_message(message.chat.id, "https://github.com/kkkk4444")

@bot.message_handler(commands=['arthas'])
def arthas(message):
        bot.send_message(message.chat.id, 'https://www.youtube.com/channel/UCbt5BCs0aUDgNwRaUnKtXwA')


@bot.message_handler(commands=['yandex'])
def yandex(message):
        bot.send_message(message.chat.id, 'yandex.ru')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Здравствуй')
    elif message.text.lower() == 'кто ты':
        bot.send_message(message.chat.id, 'Я робот')
    elif message.text.lower() == 'забей':
        bot.send_message(message.chat.id, 'wo?')
    else:
        bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')




bot.polling()