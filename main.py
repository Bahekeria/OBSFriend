import telebot as telebot
from telebot import types


bot = telebot.TeleBot('7106311480:AAHo8AXLHQ7NEx9l0rZR2pufSig8p_cYV6A')
tag_teams, tag_score, tag_time, tag_round = False, False, False, False                  # Первичные флаги
time_irl, time_time = False, False                                                      # Флаги времени
change_tag, change_time, game, local_check = False, False, False, False                 # Cache-переменные
the_text = ''                                                                           # Любой, мать его, текст
# ws = obsws("localhost", 4444)                                                         # Связь с OBS
# ws.connect()                                                                          # Связь с OBS
# usefuls = '✔''✖'
# filename =  "https://github.com/Kevinjareczek/CSCI490/blob/master/traininglabels.txt" # Так Гитхаб можно ковырять
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
    response = requests.put(f"https://api.github.com/repos/{USERNAME}/{repo_name}/contents/{file_name}", 
            headers=headers, data=json.dumps(data))
    pprint(response.json())
'''


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    global tag_teams, tag_score, tag_time, tag_round
    tag_teams, tag_score, tag_time, tag_round = False, False, False, False
    button1 = types.InlineKeyboardButton('Настроить трансляцию', callback_data='setup_step_0')
    button2 = types.InlineKeyboardButton('Инструкция для первичной настройки', callback_data='first_steps')
    button3 = types.InlineKeyboardButton('МВ 11-12.05.2024 ТЕСТ', callback_data='the_game')
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    bot.send_message(message.chat.id, f'Привет!\n\nЯ – ваш главный помощник для проведения трансляций через сервис OBS.'
                                      f' \n\n<i>С чего начнём?</i>', parse_mode='html', reply_markup=markup)


'''
@bot.callback_query_handler(func=lambda callback: True)
def users_all(callback):
    global tag_teams, tag_score, tag_time, tag_round, change_tag
    global time_irl, time_time, change_time, local_check
    global the_text, game
    
    if callback.data == 'setup_step_0' or callback.data == 'change_tag_teams' or callback.data == 'change_tag_score' \
            or callback.data == 'change_tag_time' or callback.data == 'change_tag_round':
        markup = types.InlineKeyboardMarkup()
        bot.delete_message(callback.message.chat.id, callback.message.id)
        time_irl, time_time = False, False

        if callback.data == 'change_tag_teams':
            tag_teams = not tag_teams 
        if callback.data == 'change_tag_score':
            tag_score = not tag_score 
        if callback.data == 'change_tag_time':
            tag_time = not tag_time 
        if callback.data == 'change_tag_round':
            tag_round = not tag_round 

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
        if tag_round:
            button4 = types.InlineKeyboardButton('Этап: ✔', callback_data='change_tag_round')
        else:
            button4 = types.InlineKeyboardButton('Этап: ✖', callback_data='change_tag_round')

        change_tag = False if not tag_teams and not tag_score and not tag_time and not tag_round else True

        if tag_time:
            button5 = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_1')
        else:
            button5 = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_2')
        button6 = types.InlineKeyboardButton('Вернуться в начало', callback_data='start_the_bot')
        markup.row(button1)
        markup.row(button2, button3, button4)
        markup.row(button5)
        markup.row(button6)
        bot.send_message(callback.message.chat.id, f'Для начала <b>выберите</b>, что пригодится Вам для проведения '
                                                   f'трансляции', parse_mode='html', reply_markup=markup)
    
    elif callback.data == 'setup_step_1' and not change_tag:
        markup = types.InlineKeyboardMarkup()
        bot.delete_message(callback.message.chat.id, callback.message.id)
        button1 = types.InlineKeyboardButton('Названия команд: ✖', callback_data='change_tag_teams')
        button2 = types.InlineKeyboardButton('Счёт: ✖', callback_data='change_tag_score')
        button3 = types.InlineKeyboardButton('Время: ✖', callback_data='change_tag_time')
        button4 = types.InlineKeyboardButton('Этап: ✖', callback_data='change_tag_round')
        button5 = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_1')
        button6 = types.InlineKeyboardButton('Вернуться в начало', callback_data='start_the_bot')
        markup.row(button1)
        markup.row(button2, button3, button4)
        markup.row(button5)
        markup.row(button6)
        bot.send_message(callback.message.chat.id, f'Просим Вас не торопиться и <b>выбрать</b>, что пригодится Вам для'
                                                   f' проведения трансляции:', parse_mode='html', reply_markup=markup)

    elif (callback.data == 'CHANGE_IT:setup_step_1' and tag_time) \
            or callback.data == 'change_time_irl' or callback.data == 'change_time_time':
        markup = types.InlineKeyboardMarkup()
        bot.delete_message(callback.message.chat.id, callback.message.id)

        if callback.data == 'change_time_irl':
            time_irl = not time_irl
            if time_irl and time_time:
                time_time = not time_time
            bot.delete_message(callback.message.chat.id, callback.message.id)
        if callback.data == 'change_time_time':
            time_time = not time_time
            if time_irl and time_time:
                time_irl = not time_irl
            bot.delete_message(callback.message.chat.id, callback.message.id)

        if time_irl:
            button1 = types.InlineKeyboardButton('Текущее время (UTC +3): ✔', callback_data='change_time_irl')
        else:
            button1 = types.InlineKeyboardButton('Текущее время (UTC +3): ✖', callback_data='change_time_irl')
        if time_time:
            button2 = types.InlineKeyboardButton('Время тайма: ✔', callback_data='change_time_time')
        else:
            button2 = types.InlineKeyboardButton('Время тайма: ✖', callback_data='change_time_time')

        change_time = True if time_irl or time_time else False
        if tag_time and change_time:
            button3 = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_2')
        else:
            button3 = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_1')
        button4 = types.InlineKeyboardButton('Вернуться назад', callback_data='setup_step_0')
        markup.row(button1, button2)
        markup.row(button3)
        markup.row(button4)
        bot.send_message(callback.message.chat.id, f'Пожалуйста, уточните, какое конкретно время вам нужно?\n\n'
                                                   f'Выберите один из вариантов <b>ниже</b>.'
                                                   f'', parse_mode='html', reply_markup=markup)

    elif callback.data == 'setup_step_2':
        markup = types.InlineKeyboardMarkup()
        bot.delete_message(callback.message.chat.id, callback.message.id)
        if local_check:
            button4 = types.InlineKeyboardButton('Перейти к игре', callback_data='the_game')
            markup.row(button4)
            bot.send_message(callback.message.chat.id, f'Настройка завершена!', reply_markup=markup)
        else:
            if tag_teams:
                the_text = ''
                with open("team_1.txt", "r") as file_team_1:
                    the_text += file_team_1.read()
                the_text += ' — '
                with open("team_2.txt", "r") as file_team_2:
                    the_text += file_team_2.read()

                with open("team_1.txt", "r") as file_team_1:
                    the_text = ''
                    the_text += file_team_1.read()
                    if the_text != '':
                        with open("team_2.txt", "r") as file_team_2:
                            the_text = ''
                            the_text += file_team_2.read()
                            local_check = True if the_text != '' else False
                    else:
                        local_check = False

                if the_text == ' — ':
                    button1 = types.InlineKeyboardButton('Установить названия команд', callback_data='setup_teams')
                else:
                    button1 = types.InlineKeyboardButton(f'{the_text}. Исправить?', callback_data='setup_teams')
                markup.row(button1)
            if tag_score:
                the_text = ''
                with open("score_1.txt", "r") as file_score_1:
                    the_text += file_score_1.read()
                the_text += ' : '
                with open("score_2.txt", "r") as file_score_2:
                    the_text += file_score_2.read()

                with open("score_1.txt", "r") as file_score_1:
                    the_text = ''
                    the_text += file_score_1.read()
                    if the_text != '':
                        with open("score_2.txt", "r") as file_score_2:
                            the_text = ''
                            the_text += file_score_2.read()
                            local_check = True if the_text != '' else False
                    else:
                        local_check = False

                if the_text == ' : ':
                    button2 = types.InlineKeyboardButton('Установить счёт', callback_data='setup_score')
                else:
                    button2 = types.InlineKeyboardButton(f'{the_text}. Исправить?', callback_data='setup_teams')
                markup.row(button2)
            if tag_round:
                the_text = ''
                with open("type.txt", "r") as file_round:
                    the_text += file_round.read()

                with open("round_1.txt", "r") as file_round_1:
                    the_text = ''
                    the_text += file_round_1.read()
                    local_check = True if the_text != '' else False

                if the_text == '':
                    button3 = types.InlineKeyboardButton('Установить раунд', callback_data='setup_round')
                else:
                    button3 = types.InlineKeyboardButton(f'{the_text}. Исправить?', callback_data='setup_teams')
                markup.row(button3)
            bot.send_message(callback.message.chat.id, f'Отлично! Переходим к данным.\n\n'
                                                       f'Выберите, что вы хотите настроить:'
                                                       f'', parse_mode='html', reply_markup=markup)

    elif callback.data == 'setup_teams':
        markup = types.InlineKeyboardMarkup()
        bot.send_message(callback.message.chat.id, f'Введите название первой команды:')
        the_text = ''
        while the_text == '':
            bot.register_next_step_handler(callback.message, to_file)
            break
        with open("team_1.txt", "w") as file_team_1:
            file_team_1.write(the_text)
        bot.send_message(callback.message.chat.id, f'Введите название второй команды:')
        the_text = ''
        while the_text == '':
            bot.register_next_step_handler(callback.message, to_file)
            break
        with open("team_2.txt", "w") as file_team_2:
            file_team_2.write(the_text)
        if game:
            button = types.InlineKeyboardButton('Вернуться к игре', callback_data='the_game')
        else:
            button = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_2')
        markup.row(button)
        bot.send_message(callback.message.chat.id, f'Названия команд успешно получены.', reply_markup=markup)

    elif callback.data == 'setup_score':
        markup = types.InlineKeyboardMarkup()
        bot.send_message(callback.message.chat.id, f'Введите количество очков первой команды:')
        the_text = ''
        while the_text == '':
            bot.register_next_step_handler(callback.message, to_file)
            break
        if not the_text.isdigit():
            bot.send_message(callback.message.chat.id, f'Пожалуйста, введите числовое значение:')
            the_text = ''
            while the_text == '':
                bot.register_next_step_handler(callback.message, to_file)
                break
        with open("score_1.txt", "w") as file_score_1:
            file_score_1.write(the_text)
        bot.send_message(callback.message.chat.id, f'Введите количество очков второй команды:')
        the_text = ''
        while the_text == '':
            bot.register_next_step_handler(callback.message, to_file)
            break
        if not the_text.isdigit():
            bot.send_message(callback.message.chat.id, f'Пожалуйста, введите числовое значение:')
            the_text = ''
            while the_text == '':
                bot.register_next_step_handler(callback.message, to_file)
                break
        with open("score_2.txt", "w") as file_score_2:
            file_score_2.write(the_text)
        if game:
            button = types.InlineKeyboardButton('Вернуться к игре', callback_data='the_game')
        else:
            button = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_2')
        markup.row(button)
        bot.send_message(callback.message.chat.id, f'Счёт задан.', reply_markup=markup)
            
    elif callback.data == 'setup_round':
        markup = types.InlineKeyboardMarkup()
        bot.send_message(callback.message.chat.id, f'Введите раунд:')
        the_text = ''
        while the_text == '':
            bot.register_next_step_handler(callback.message, to_file)
            break
        with open("round.txt", "w") as file_round:
            file_round.write(the_text)
        if game:
            button = types.InlineKeyboardButton('Вернуться к игре', callback_data='the_game')
        else:
            button = types.InlineKeyboardButton('Продолжить настройку', callback_data='setup_step_2')
        markup.row(button)
        bot.send_message(callback.message.chat.id, f'Текущий раунд указан.', reply_markup=markup)
'''


@bot.callback_query_handler(func=lambda callback: True)
def users_all(callback):
    if callback.data == 'the_game' or callback.data == 'goal_1' or callback.data == 'goal_2':
        # game = True
        markup = types.InlineKeyboardMarkup()
        bot.delete_message(callback.message.chat.id, callback.message.id)
        global the_text

        '''
        if tag_teams:
            the_text += '\n<b>Команды</b>: '
            with open("team_1.txt", "r") as file_team_1:
                the_text += file_team_1.read()
                the_text += ' — '
                with open("team_2.txt", "r") as file_team_2:
                    the_text += file_team_2.read()
            button1 = types.InlineKeyboardButton('Изменить команды', callback_data='setup_teams')
            markup.row(button1)

        if tag_score:
            the_text += '\n<b>Счёт</b>: '
            with open("score_1.txt", "r") as file_score_1:
                the_text += file_score_1.read()
                the_text += ' — '
                with open("score_2.txt", "r") as file_score_2:
                    the_text += file_score_2.read()
            button2 = types.InlineKeyboardButton('Гол 1', callback_data='goal_1')
            button3 = types.InlineKeyboardButton('Изменить', callback_data='setup_score')
            button4 = types.InlineKeyboardButton('Гол 2', callback_data='goal_2')
            markup.row(button2, button3, button4)

        if tag_round:
            the_text += '\n<b>Раунд</b>: '
            with open("round_1.txt", "r") as file_round_1:
                the_text += file_round_1.read()
            button5 = types.InlineKeyboardButton('Изменить раунд', callback_data='setup_round')
            markup.row(button5)
        '''

        if callback.data == 'goal_1':
            with open("score_1.txt", "a") as file_score_1:
                score = int(file_score_1.read())
                score += 1
                file_score_1.read(score)

        if callback.data == 'goal_2':
            with open("score_2.txt", "a") as file_score_2:
                score = int(file_score_2.read())
                score += 1
                file_score_2.read(score)

        the_text += '\n\n<b>Счёт</b>: '
        with open("score_1.txt", "r") as file_score_1:
            the_text += file_score_1.read()
            the_text += ' — '
            with open("score_2.txt", "r") as file_score_2:
                the_text += file_score_2.read()
        button2 = types.InlineKeyboardButton('Гол 1', callback_data='goal_1')
        button3 = types.InlineKeyboardButton('Изменить', callback_data='setup_score')
        button4 = types.InlineKeyboardButton('Гол 2', callback_data='goal_2')
        markup.row(button2, button3, button4)
        '''
        button6 = types.InlineKeyboardButton('Вернуться в начало', callback_data='game_stop_confirmation')
        markup.row(button6)
        '''
        bot.send_message(callback.message.chat.id, f'Идёт игра. {the_text}', parse_mode='html', reply_markup=markup)

    elif callback.data == 'game_stop_confirmation':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Вернуться к игре', callback_data='the_game')
        button2 = types.InlineKeyboardButton('Сбросить данные', callback_data='start_the_bot')
        markup.row(button1, button2)
        bot.send_message(callback.message.chat.id, f'Подумайте хорошенько. Вы точно хотите вернуться в начало?'
                                                   f'\n\n<b>Данные не сохранятся!</b>'
                                                   f'', parse_mode='html', reply_markup=markup)

    elif callback.data == 'start_the_bot':
        bot.delete_message(callback.message.chat.id, callback.message.id)
        tag_teams, tag_score, tag_time, tag_round = False, False, False, False
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Настроить трансляцию', callback_data='setup_step_0')
        button2 = types.InlineKeyboardButton('Инструкция для первичной настройки', callback_data='readme')
        markup.row(button1, button2)
        bot.send_message(callback.message.chat.id,
                         f'Привет!\n\nЯ – ваш главный помощник для проведения трансляций через сервис OBS.'
                         f' \n\n<i>С чего начнём?</i>', parse_mode='html', reply_markup=markup)
        
    elif callback.data == 'readme':
        bot.delete_message(callback.message.chat.id, callback.message.id)
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Перейти к настройке', callback_data='setup_step_0')
        markup.row(button)
        bot.send_message(callback.message.chat.id, 'Напишу, напишу. Надо не забыть.', reply_markup=markup)


def to_file(message):
    global the_text
    while the_text == '':
        the_text = str(message.text)
        break


bot.infinity_polling()

# Данная версия является разработкой специально для проведения матчей на Коробке МФТИ
# By Bahekeria
