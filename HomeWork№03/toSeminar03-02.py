#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
#- [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

import os
import random
import math

def main():
    os.system('CLS')
    print_message()
    volume = create_volume()
    list1 = fill_list (volume)
    list_and_mult_pairs(list1)
    
def print_message():
    print('\nБудет сгенерирован список из чисел от 1 по 10. Кол-во чисел от 3 по 9 - для наглядности.')#Что делаем    
    
def create_volume() -> int:
    volume = random.randint(3,9)#Определяем кол-во элементов списка (для наглядности  от 3 по 9)
    return volume

def fill_list(volume : int ) -> int:
    listOfNumbers = []#Заполняем с помощью генерации исходный список (для наглядности числами от 1 по 10).
    i = 0
    while( i < volume):
        temp = random.randint(1,10)
        listOfNumbers.append(temp) 
        i+=1
    print(f'\nИсходный сгенерированный список : {listOfNumbers}')
    return listOfNumbers
    
def list_and_mult_pairs (list1 : int):
    list2 = []#Список из произведение пар крайних чисел исходного списка
    list3 = []#Список из пар крайних чисел исходного списка
    i = 0
    while(i < (len(list1) / 2)):
        list3.append(f'{list1[i]} * {list1[len(list1) - 1 - i]}')
        list2.append(list1[i] * list1[len(list1) - 1 - i])
        i+=1
    print(f'\nСписок из пар крайних чисел исходного списка : {list3}\n')
    print(f'Список из произведение пар крайних чисел исходного списка : {list2}\n')
        
main()# Вызов функции main