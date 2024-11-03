import telebot
from caption_to_image import generate_image, create_file_name
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

tg_group = os.getenv('TG_GROUP')
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ предлагаю загрузить свою картинку")


@bot.message_handler(content_types=["photo"])
def image_handler(message):
    global tmp

    user_id = message.from_user.id
    photo = message.photo[-1]

    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    tmp = create_file_name(user_id)

    with open(tmp, 'wb') as new_file:
        new_file.write(downloaded_file)
    generate_image(tmp)
    changed_photo = open(tmp, 'rb')
    bot.send_photo(message.chat.id, photo=changed_photo)
    create_keyboard(message)


@bot.message_handler(commands=['text'])
def create_keyboard(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_share = types.KeyboardButton('Поделиться')
    keyboard.add(button_share, )
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global tmp
    print(tmp)
    if message.text == 'Поделиться' and tmp:
        # Действия при нажатии на кнопку Поделиться
        photo = open(tmp, 'rb')
        bot.send_photo(chat_id=tg_group, photo=photo)
        tmp = ''
        bot.reply_to(message, 'Фотография успешно отправлена, можете загрузить другую фотографию',
                     reply_markup=types.ReplyKeyboardRemove())


tmp = ''
print('Бот запущен')
bot.infinity_polling()
