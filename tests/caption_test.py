from datetime import datetime

import pytest
import os
from caption_to_image import create_file_name, get_caption
from dotenv import load_dotenv

load_dotenv()
images_folder = os.getenv('IMAGES_FOLDER')


@pytest.fixture
def get_file_name():
    return create_file_name(user_id=123)


@pytest.mark.parametrize('user_id', [123, 456])
def test_create_file_name(user_id):
    image_name = create_file_name(user_id)
    now = datetime.now()
    assert isinstance(image_name, str)
    assert image_name == f'{images_folder}{now.strftime("%Y-%M-%d_%H:%M")}_{user_id}.jpg'


@pytest.mark.xfail
def test_create_wrong_file_name(user_id=123):
    image_name = create_file_name(user_id)
    now = datetime.now()
    assert image_name == f'{images_folder}{now.strftime("%Y-%M-%d_%H:%M")}_124.jpg'


def test_create_random_caption():
    caption = get_caption('./captions.txt')
    assert len(caption) > 0
    assert isinstance(caption, str)
