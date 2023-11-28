import telebot

bot = telebot.TeleBot('6074138054:AAGrN8Mt2yX7GlDiZBNfE-kQOYsEVXBxw0E')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сессия,сдай себя сама,пожалуйста')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Да поможет тебе Бог! \nСпаси и сохрани!')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id,
                     'ПОСЛЕДНЯЯ НАДЕЖДА [ССЫЛКА](https://new.online-chasovnya.ru/category/postavit-svechku/besplatno/)',
                     parse_mode='Markdown')


bot.infinity_polling()