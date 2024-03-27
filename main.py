import requests
from bs4 import BeautifulSoup as b
import telebot
import random

URL = 'https://www.anekdot.ru/release/anekdot/year/2023/9'
API_KEY = '6834689780:AAGZSLXnTOhbyR9RtBkkx8nRRDvLormeAvY'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, choose number for cringe')

@bot.message_handler(content_types=['text'])
def jokes_handler(message):
    if message.text in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите цифру')
print(list_of_jokes)
bot.polling()

