import telegraph_api as state
from telegraph_api import Telegraph
import asyncio


# Declaring asynchronous function for using await
async def main():
    # Creating new Telegraph object
    telegraph = Telegraph()
    # Creating new account
    await telegraph.create_account("My Favourite Blog", author_name="Ivan")
    # Creating new page
    new_page = await telegraph.create_page(
        "My first Telegraph Post",
        content_html="<p>Hello world!</p>" # Html content can be presented
    )
    # Printing page url into console
    print(new_page.url)


# Running asynchronous function
asyncio.run(main())

'''
Можно брать несколько пикселей с картинки и проверять их цвет, и если 2 секунды они равнозначны – пиздец

Вернуться к предыдущему этапу – добавить UI дерево

Инструкция – сделать в последнюю очередь

Бесконечный Git commit – полная хуйня, надо реализовывать всё через телегу и внутреннюю html экосистему

SQL? Хз. Поискать опен сорс.

Не забыть про изображение базовой плашки и про форматирование шрифта

Добавить ещё одно время в базовый прототип: время матча/тайма

Опционально: добавить мануал по проведению трансляций

Блять, vk api... Подвязка комментариев.

Точно! Статьи в телеге!!!! Боже это же волшебно. Господи, та идея, которая мне была так нужна, ааааааааааа

Изучить возможность раздельного отправления сообщений ботом в те или иные чаты и определённую модерацию

Screensaver – миф или реальность? Возможно ли научить бота отправлять видео(кружочки)?

Подумать над реализацией музыки
'''