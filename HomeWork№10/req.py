import requests, json

#res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

result = json.loads(res.text)

print(result['Valute']["USD"]['Name'], result['Valute']["USD"]['Value'])
print(result['Valute']["EUR"]['Name'], result['Valute']["EUR"]['Value'])
