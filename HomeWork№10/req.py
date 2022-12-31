import requests, json
from datetime import date

#res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
dates = ['AUD' ,'AZN','GBR','AZN','AMD','BGN','EUR','JPY','USA','CAD','UAH']
result = json.loads(res.text)
today = date.today()
temp2 = "{}.{}.{}".format(today.day, today.month, today.year)     
print(f' На {temp2} курс валют :')  
print(result['Valute']["USD"]['Name'], result['Valute']["USD"]['Value'])
print(result['Valute']["EUR"]['Name'], result['Valute']["EUR"]['Value'])
#print(len(result))
#print(result.keys())
print(result['Valute']['EUR']['NumCode'])
print(list(result['valute']))
