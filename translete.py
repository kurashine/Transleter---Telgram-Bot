import telebot
from translate import Translator

# Вставьте ваш токен Telegram-бота
bot_token = '6182864197:AAFTe_fWFnT20E09y8oFbRiiiQzRAViQaUI'

# Создаем экземпляр класса TeleBot
bot = telebot.TeleBot(bot_token)

# Обработчик команды /start


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, 'Привет! Я бот-переводчик. Просто отправьте мне текст, и я переведу его.')

# Обработчик текстовых сообщений


@bot.message_handler(func=lambda message: True)
def translate_text(message):
    text = message.text
    # Переводим текст на английский
    translator = Translator(to_lang='en', from_lang='ru')
    translated_text = translator.translate(text)
    bot.reply_to(message, translated_text)


# Запускаем бота
bot.polling()
