#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет
import os
os.system('CLS')
weekDays = ["Понедельник", "Вторник", "Среда","Четверг", "Пятница", "Суббота", "Воскресенье"]
i = 0
while i < len(weekDays):
    print(i+1,' - ',weekDays[i])
    i+=1
numberOfDay = int( input('\t   Введите порядковый номер дня недели : '))
if(numberOfDay<0 or numberOfDay>7):
    print('неправильный ввод')
else:
    print(numberOfDay,' - ',weekDays[numberOfDay-1])
    if(numberOfDay==6 or numberOfDay==7):
         print('\tЭто выходной\n')
    else:
         print('\tЭто рабочий день\n')
