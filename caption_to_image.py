from PIL import Image, ImageDraw, ImageFont
from random import choice
from datetime import datetime
import os
from make_caption_file import make_caption_file
from dotenv import load_dotenv


load_dotenv()


images_folder = os.getenv('IMAGES_FOLDER')
file_with_captions = os.getenv('FILE_WITH_CAPTIONS')


def create_file_name(user_id):
    now = datetime.now()
    file_name = f'{images_folder}{now.strftime("%Y-%M-%d_%H:%M")}_{user_id}.jpg'
    return file_name


def get_caption(file_name):
    try:
        with open(file_name, 'r') as file:
            captions = file.read().splitlines()
        caption = choice(captions)
        return caption
    except FileNotFoundError:
        make_caption_file()
        return get_caption(file_name)


def generate_image(image_name):

    caption = get_caption(file_with_captions)

    image = Image.open(image_name)
    drawer = ImageDraw.Draw(image)

    image_width, image_height = image.size
    font_size = int(image_width / 12)
    x = image_width // 6
    y = image_height - font_size - 100
    font = ImageFont.truetype('Lobster.ttf', size=font_size)

    # Рисуем контур текста
    drawer.text((x - 3, y), text=caption, font=font, fill='black')  # Левый сдвиг
    drawer.text((x + 5, y), text=caption, font=font, fill='grey')  # Правый сдвиг
    drawer.text((x, y - 3), text=caption, font=font, fill='black')  # Верхний сдвиг
    drawer.text((x, y + 5), text=caption, font=font, fill='grey')  # Нижний сдвиг

    # Рисуем текст
    drawer.text((x, y), text=caption, font=font, fill='white')

    image.save(image_name)
