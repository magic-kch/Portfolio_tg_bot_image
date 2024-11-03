# Установка базового образа с вашей текущей версией Python (3.7)
FROM python:3.10.12

# Установка необходимых зависимостей
RUN apt-get update && apt-get install -y git

# Клонирование проекта с GitHub
RUN git clone https://github.com/username/repository.git /tg_bot_image

# Установка дополнительных зависимостей, если необходимо
RUN pip install -r /tg_bot_image/requirements.txt

# Определение рабочей директории
WORKDIR /tg_bot_image

# Команда запуска приложения
CMD ["python", "main.py"]