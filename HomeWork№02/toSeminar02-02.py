#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print ('\033[34m{}') #Цвет шрифта - синий <34m>
import os
os.system('CLS')
number = input('Введите число N : ')
os.system('CLS')
os.system('type 02-01.txt')
print(f'\n\tВведено число N равное {number} , тогда набор произведений чисел от 1 до N будет равен :\n ')
listMultiplication = [] # Список для хранения набора произведений чисел
temp = range (1, (int(number) + 1)) #Коллекция последовательных чисел
mult = temp[0]
for i in temp:
    listMultiplication.append( mult * temp[i - 1])
    print(f'\tN = {i} {listMultiplication}')
    mult = mult * temp[i - 1] 
print ('\033[31m{}' .format('\tУдачи !')) #Цвет шрифта красный <31> 
print('\033[0m')#Возврат стандартного цвета шрифта  