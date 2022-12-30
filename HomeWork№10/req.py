import requests, json
from datetime import date

#res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

result = json.loads(res.text)
today = date.today()
temp2 = "{}.{}.{}".format(today.day, today.month, today.year)     
print(f' На {temp2} курс валют :')  
print(result['Valute']["USD"]['Name'], result['Valute']["USD"]['Value'])
print(result['Valute']["EUR"]['Name'], result['Valute']["EUR"]['Value'])
