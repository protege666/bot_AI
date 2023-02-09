import openai
import telebot
import dotenv
import os

dotenv.load_dotenv('.env')

openai.api_key = os.environ['API_KEY']
bot = telebot.TeleBot(os.environ['BOT_KEY'])


@bot.message_handler(commands=['start'])
def welcome_start(message):
    bot.send_message(
        message.chat.id, f'Приветствую тебя, {message.chat.first_name}.\n\nЯ Вероника - искуственный интелект. Пока что я нахожусь в демо версии, но мы уже сейчас можем пообщаться!')


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    if message.text == '/start':
        bot.send_message(
            message.chat.id, f'Приветствую тебя, {message.chat.first_name}')
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        bot.send_message(chat_id=message.from_user.id,
                         text=response['choices'][0]['text'])


print('bot running')
bot.polling()
