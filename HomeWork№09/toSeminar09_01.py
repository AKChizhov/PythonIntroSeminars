import telebot, config , os
from random import randint
from random import choice

bot = telebot.TeleBot(config.TOKEN)
candys = dict()
enable_game = dict()
who_fierst = dict()

os.system('cls')

def handle_game_proc(message):
    global enable_game
    
    try:
        if (enable_game[message.chat.id] and 1 <= int(message.text) <= max_move): return True
        else: return False
    except KeyError:
        enable_game[message.chat.id] = False
        if (enable_game[message.chat.id] and 1 <= int(message.text) <= max_move ): return True
        else: return False

@bot.message_handler(commands=['sg'])
def send_welcome(message):
    print('\t Играем в конфеты')
    global who_fierst, candys, enable_game, max_move, max_candys
    max_move = 28
    max_candys = 117
    bot.reply_to(message, f'Начинаем игру в конфеты, на столе {max_candys} берем не больше { max_move} шт. за ход')
    candys[message.chat.id] = max_candys
    who_fierst[message.chat.id] = choice(['Bot', 'Вы'])
    bot.send_message(message.chat.id, f'Начинает игру в конфеты {who_fierst[message.chat.id]}')
    enable_game[message.chat.id] = True
    if who_fierst[message.chat.id] == 'Bot':
        how_much_candys = randint(1, candys[message.chat.id] % (max_move + 1))
        candys[message.chat.id] -= how_much_candys
        bot.send_message(message.chat.id, f'Бот взял со стола конфет {how_much_candys}')
        bot.send_message(message.chat.id,f'Осталось конфет на столе {candys[message.chat.id]}')
        who_fierst[message.chat.id] = 'Вы'

@bot.message_handler(func=handle_game_proc)
def game_process(message):
    global candys, who_fierst, enable_game
    if who_fierst[message.chat.id] == 'Вы':
        if candys[message.chat.id] > max_move:
            candys[message.chat.id] -= int(message.text)
            bot.send_message(message.chat.id,f'Осталось на столе конфет {candys[message.chat.id]} Ваш ход')
            if candys[message.chat.id] > max_move:
                temp = candys[message.chat.id] % (max_move + 1)
                if temp == 0 : how_much_candys = randint(1, max_move)
                else : how_much_candys = randint(1, temp)
                candys[message.chat.id] -= how_much_candys
                bot.send_message(message.chat.id, f'Бот взял со стола конфет {how_much_candys}')
                bot.send_message(message.chat.id, f'Осталось на столе конфет  {candys[message.chat.id]} Ваш ход')
                if candys[message.chat.id] <= max_move:
                    bot.send_message(message.chat.id, 'Вы победили')
                    enable_game[message.chat.id] = False
            else:
                bot.send_message(message.chat.id, 'Bot победил')
                enable_game[message.chat.id] = False
        else:
            bot.send_message(message.chat.id, 'Bot победил')
            enable_game[message.chat.id] = False

bot.infinity_polling()
