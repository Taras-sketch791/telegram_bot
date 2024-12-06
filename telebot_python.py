#pip install pyTelegramBotAPI
# https://t.me/BotFather
# https://t.me/kbvfdhhkjkeyjbot

import telebot

bot = telebot.TeleBot("7940044719:AAFsqm4qVz6e8LCQbFPELrXk4-VR8D0HY-8")


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, f'You wrote me: {message.text}!')


bot.infinity_polling()

