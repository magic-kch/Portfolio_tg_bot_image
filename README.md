# Разработка телеграм бота с редактированием изображений
### Бот получает от пользователя картинку, выбирает из файла-сборника случайную подпись и рисует её на картинке пользователя. Полученную картинку бот отправляет пользователю и предлагает ей поделиться.

Бот реализован на языке Python.
Все настройки бот должен брать из переменных окружения.
Картинки пользователя бот сохраняет в папку (путь до неё настраивается) с именем в формате «YYYY-MM-DD_HH:mm_user id.jpg».

__YYYY__ — год, четыре знака,

__MM__ — месяц, два знака,

__DD__ — день, два знака,

__HH__ — часы, 24 часовой формат, два знака,

__mm__ — минуты, два знака,

__user id__ — id пользователя, приславшего фото

* Если пользователь согласен поделиться картинкой — бот репостит её в канал, который указан в настройках бота.
 
* Файл-сборник имеет текстовый формат, каждая фраза занимает отдельную строку. Путь до файла-сборника указывается в настройках. Если файла нет, он создаться автоматически.

Для запуска бота необходимо:

1. Установить зависимости
    ```pip install -r reqirements.txt```

2. Переименовать файл переменных окружения
   ```mv _env .env```

3. Внести свои значения `.env`
   ```
   # токен вашего телеграм бота
   TOKEN=ТОКЕН_ВАШЕГО_ТЕЛЕГРАМ_БОТА
   # id группы в телеграме
   TG_GROUP=-100ХХХХХХХХХХХ 
   # название папки куда бот будет сохранять # изменненые фотографии
   IMAGES_FOLDER=./images/  
   # название файла с подписями, если его не будет скрипт сам создаст его                           
   FILE_WITH_CAPTIONS=captions.txt 
   ```

#### Для автоматического развертывания присутствует Dockerfile
