import telebot
import config
import cinemabot_lib.scrapper

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_command(message):
    start_message = 'Cinemabot v1.0:\n' \
                     '/help - show commands and usage'
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['help'])
def help_command(message):
    help_message = 'commands:\n'\
                   '/help\n' \
                   '/start\n' \
                   '[$YOUR_MOVIE]'
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(content_types=['text'])
def send_text(message):
    desc, url = cinemabot_lib.scrapper.search_movie(message.text)
    bot.send_chat_action(chat_id=message.chat.id, 'typing')
    bot.send_message(message.chat.id, desc)
    bot.send_photo(chat_id=message.chat.id, photo=url)


def main():    
    bot.polling()


if __name__ == '__main__':
    main()
