import config
import telebot

bot = telebot.TeleBot(config.token)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

import urllib
from bs4 import BeautifulSoup
import requests
import urllib.request
from imdb import IMDb
import re

ia = IMDb()

@bot.message_handler(content_types=['text'])
def send_text(message):
    movies = ia.search_movie(message.text)
    movie = movies[0]
    ia.update(movie, info=['main', 'plot', 'taglines', 'vote details'])

    #text = urllib.parse.quote_plus(message.text + 'смотреть онлайн')
    #url = 'https://google.com/search?q=' + text

    #response = requests.get(url)

    #soup = BeautifulSoup(response.text, 'lxml')
    #urls = []
    #for g in soup.find_all("div", class_="kCrYT"):
    #    for t in g.find_all("a", href=True):
    #        if t['href'][:7] != '/search':
    #            urls.append(t['href'][7:])

   # bot.send_message(message.chat.id, '\n'.join(urls[:5]))
    bot.send_message(message.chat.id, movie.get('title') + ' ' + str(movie.get('arithmetic mean')))
    bot.send_message(message.chat.id, re.split(r'::', movie.get('plot')[0],maxsplit=1)[0])
    bot.send_photo(chat_id=message.chat.id, photo=movie['full-size cover url'])

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

def main():    
    bot.polling()

if __name__ == '__main__':
    main()
