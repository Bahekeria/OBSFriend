import telebot as telebot
from telebot import types
import pandas as pd


bot = telebot.TeleBot('7106311480:AAHo8AXLHQ7NEx9l0rZR2pufSig8p_cYV6A')
tag_teams = False
tag_score = False
tag_time = False
tag_type = False
# usefuls = '✔''✖'
# filename =  "https://github.com/Kevinjareczek/CSCI490/blob/master/traininglabels.txt" ← Так Гитхаб можно ковырять
'''
def create_repo(repo_name, file_name, file_content):
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"token {TOKEN}"}
    data = {'name': repo_name}
    r = requests.post("https://api.github.com/user/repos", headers=headers, data=json.dumps(data))
    print("Repo created")

    data = {
        'message': 'Initial commit', 
        'content': b64encode(file_content.encode('utf-8')).decode('utf-8'), 
    }
    response = requests.put(f"https://api.github.com/repos/{USERNAME}/{repo_name}/contents/{file_name}", headers=headers, data=json.dumps(data))
    pprint(response.json())
'''

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Настроить трансляцию', callback_data='setup_step_0')
    button2 = types.InlineKeyboardButton('Инструкция для первичной настройки', callback_data='first_steps')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, f'Привет!\nЯ – ваш главный помощник для проведения трансляций через сервис OBS.'
                                      f' <i>С чего начнём?</i>', parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def users_all(callback):
    global tag_teams
    global tag_score
    global tag_time
    global tag_type
    if callback.data == 'setup_step_0' or callback.data == 'change_tag_teams' or callback.data == 'change_tag_score' \
            or callback.data == 'change_tag_time' or callback.data == 'change_tag_type':
        markup = types.InlineKeyboardMarkup()

        if callback.data == 'change_tag_teams':
            tag_teams = not tag_teams
            bot.delete_message(callback.message.chat.id, callback.message.id)
        if callback.data == 'change_tag_score':
            tag_score = not tag_score
            bot.delete_message(callback.message.chat.id, callback.message.id)
        if callback.data == 'change_tag_time':
            tag_time = not tag_time
            bot.delete_message(callback.message.chat.id, callback.message.id)
        if callback.data == 'change_tag_type':
            tag_type = not tag_type
            bot.delete_message(callback.message.chat.id, callback.message.id)

        if tag_teams:
            button1 = types.InlineKeyboardButton('Названия команд: ✔', callback_data='change_tag_teams')
        else:
            button1 = types.InlineKeyboardButton('Названия команд: ✖', callback_data='change_tag_teams')
        if tag_score:
            button2 = types.InlineKeyboardButton('Счёт: ✔', callback_data='change_tag_score')
        else:
            button2 = types.InlineKeyboardButton('Счёт: ✖', callback_data='change_tag_score')
        if tag_time:
            button3 = types.InlineKeyboardButton('Время: ✔', callback_data='change_tag_time')
        else:
            button3 = types.InlineKeyboardButton('Время: ✖', callback_data='change_tag_time')
        if tag_type:
            button4 = types.InlineKeyboardButton('Этап: ✔', callback_data='change_tag_type')
        else:
            button4 = types.InlineKeyboardButton('Этап: ✖', callback_data='change_tag_type')

        button5 = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_1')
        markup.row(button1)
        markup.row(button2, button3, button4)
        markup.row(button5)
        bot.send_message(callback.message.chat.id, f'Для начала <b>выберите</b>, что пригодится Вам для проведения '
                                                   f'трансляции', parse_mode='html', reply_markup=markup)
    elif callback.data == 'randomgame':
        pass
    elif callback.data == 'today':
        pass


bot.infinity_polling()
