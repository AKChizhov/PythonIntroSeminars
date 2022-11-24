#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

import os
os.system('CLS')
os.system('type 02-01.txt')

numberEnter = input('Введите вещественное число : ')
number = numberEnter.replace('.', '') #убираем (заменяем на пустое место) разделитель

summaWithFor = 0
for i in number:
    i = int(i)
    summaWithFor = summaWithFor + i
print(f'\nCумма  цифр числа {numberEnter} с использованием "for" равна {summaWithFor}')

listNumber = list(number) #из строки с числом в список строк с цифрами
listNumber= map(int, listNumber)
summaWithMap = sum(listNumber)
print(f'Cумма  цифр числа {numberEnter} с использованием "map" равна {summaWithMap}\n')
