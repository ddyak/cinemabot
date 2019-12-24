import telebot
import config
import cinemabot_lib.scrapper
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_command(message):
    start_message = 'Cinemabot v1.0:\n' \
                     '/help - show commands and usage'
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['help'])
def help_command(message):
    help_message = 'Cinemabot v1.0:\n'\
                   '/help - show this info\n'\
                   '/start - start command \n'\
                   '[$YOUR_MOVIE] - typical usage'
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_chat_action(message.chat.id, 'typing')
    desc, url = cinemabot_lib.scrapper.search_movie(message.text)
    if desc is None or url is None:
        bot.send_message(message.chat.id, 'Movie not found')
    else:
        bot.send_message(message.chat.id, desc, disable_web_page_preview=True)
        bot.send_chat_action(message.chat.id, 'typing')
        try:
            bot.send_photo(chat_id=message.chat.id, photo=url)
        except telebot.apihelper.ApiException:
            bot.send_message(message.chat.id, "Cover not found :(")


def main():
    bot.infinity_polling(True)


if __name__ == '__main__':
    main()

