import telebot, config, os, json, requests
from datetime import date
bot = telebot.TeleBot(config.TOKEN)

os.system('CLS')
dates = 'AUD ,AZN,GBR,AZN,AMD,BGN,EUR,JPY,USD,CAD,UAH'

def find(s):
    try:
        res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        result = json.loads(res.text)  
        s = s.upper()
        temp1 = str (result['Valute'][s]['Value'])
        temp3 = str (result['Valute'][s]['Name'])
        today = date.today()
        temp2 = "{}.{}.{}".format(today.day, today.month, today.year)     
        out =  str(f' На {temp2} курс {s} ({temp3}) { temp1}')
        return out # Возвращение значения
    except Exception as e:
        return (f'Данных об этой валюте НЕТ' ) # Исключение, возможное при запросе
@bot.message_handler(commands=["start"])

def start(m, res=False):
    bot.send_message(m.chat.id, f'Вводим наименование валюты без учета регистра :') 
    bot.send_message(m.chat.id, f'Например : {dates}')    
@bot.message_handler(content_types=["text"]) # Сообщение что будем искать
def handle_text(message):
    global temp
    bot.send_message(message.chat.id, find(message.text))
    temp = message.text
    print(f'Запрос на поиск курса {temp}  Программа активна')
bot.polling(none_stop=True, interval=0)
os.system('CLS')
