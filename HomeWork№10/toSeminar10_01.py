import telebot, wikipedia, re, config, os
bot = telebot.TeleBot(config.TOKEN)
wikipedia.set_lang("ru") # Устанавливаем русский язык в Wikipedia

os.system('CLS')
def getwiki(s):
    try:
        datas = wikipedia.page(s)
        wikitext_in=datas.content[:2000] # 2000 символов c начала
        wikimas=wikitext_in.split('.')
        wikimas = wikimas[:-1] # Все после последней точки удаляется
        wikitext_out = '' # Переменная для текста
        for each_strok in wikimas:
            if not('==' in each_strok): # Все без заголовков
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((each_strok.strip()))>3): wikitext_out=wikitext_out+each_strok+'.'
            else: break
        wikitext_out=re.sub('\([^()]*\)', '', wikitext_out) # Удаление разметки
        wikitext_out=re.sub('\([^()]*\)', '', wikitext_out)
        wikitext_out=re.sub('\{[^\{\}]*\}', '', wikitext_out)
        
        return wikitext_out # Возвращение текстовой строки
    except Exception as e:
        return (f'Данных об {temp} НЕТ' ) # Исключение, возможное при запросе

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Вводим слово и узнаем его значение на Wikipedia (выводится не более 2000 символов')
@bot.message_handler(content_types=["text"]) # Сообщение что будем искать
def handle_text(message):
    global temp
    bot.send_message(message.chat.id, getwiki(message.text))
    temp = message.text
    print(f'Запрос на поиск значения слова {message.text}')
bot.polling(none_stop=True, interval=0)
os.system('CLS')