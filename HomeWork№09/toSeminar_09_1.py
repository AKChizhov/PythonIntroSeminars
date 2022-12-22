import telebot
import config, os, random

bot = telebot.TeleBot(config.TOKEN)
players = ['Бот ', 'Человек']
candies = 117

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'привет ! Играем в конфеты')
  
i = 1
while(candies > 0):
    if(candies == 0) : break
    elif(candies >= 28) : frontir = 28
    else: frontir = candies
    temp = random.randint(1,frontir)
    k = 0
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, f'Ход {i} Игрока {players[0]}, на столе конфет {candies} ,он взял конфет: {temp} ')
    candies = candies - temp
    if(candies == 0) : break
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, f'Ход {i} Игрока {players[1]}, на столе конфет {candies} , сколько возмете ? ')
        global temp1
        temp1 = int(message)    
    k = 1
    candies = candies - temp      
    i+=1
 
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, f' Игрок победил {players[k]}, все конфеты его ')  
      
bot.polling(none_stop=True, interval=0)
