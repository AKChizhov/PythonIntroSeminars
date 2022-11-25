#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#Пример:
#- Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

import os
os.system('CLS')
number = int(input('Введите число N : '))
os.system('CLS')
os.system('type 02-01.txt')
print(f'\n\tВведено число N равное {number} , тогда набор чисел последовательности (1+1/N)^N от 1 до N будет равен :\n ')
listMultiplication = [] # Список для хранения набора чисел последовательности
i = 1
summ = 0
while i <= number:
    temp =round (((1 + 1 / i) ** i), 2)
    listMultiplication.append(temp) 
    summ = summ + temp
    print(f'N = {i} {listMultiplication} Их сумма равна : {summ}')
    i += 1
print('\n')