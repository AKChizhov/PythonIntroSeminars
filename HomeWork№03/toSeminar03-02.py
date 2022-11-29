#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
#- [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

import os
import random
import math

def main():
    os.system('CLS')
    volume = create_volume()
    list1 = fill_list (volume)
    number_list_mult (list1)
    list_pairs (list1)
    list_and_mult_pairs(list1)
    
def create_volume() -> int:
    volume = random.randint(3,9)
    return volume

def fill_list(volume : int ) -> int:
    listOfNumbers = []
    i = 0
    while( i < volume):
        temp = random.randint(1,10)
        listOfNumbers.append(temp) 
        i+=1
    print(f'\nИсходный сгенерированный список : {listOfNumbers}')
    return listOfNumbers
    
def number_list_mult(list1 : list) -> int:
    list2 = []
    i = 0
    while(i < (len(list1) / 2)):
        list2.append(list1[i] * list1[len(list1) - 1 - i])
        i+=1
    print(f'\nСписок из произведение пар крайних чисел исходного списка : {list2}')
    return list2

def list_pairs(list1 : list) -> str:
    list3 = []
    i = 0
    while(i < (len(list1) / 2)):
        list3.append(f'{list1[i]} * {list1[len(list1) - 1 - i]}')
        i+=1
    print(f'\nСписок из пар крайних чисел исходного списка : {list3}\n')
    return list3

def list_and_mult_pairs (list1 : int):
    list2 = []
    list3 = []
    i = 0
    while(i < (len(list1) / 2)):
        list3.append(f'{list1[i]} * {list1[len(list1) - 1 - i]}')
        list2.append(list1[i] * list1[len(list1) - 1 - i])
        i+=1
    print(f'\n\nСписок из пар крайних чисел исходного списка : {list3}\n')
    print(f'Список из произведение пар крайних чисел исходного списка : {list2}\n')
        
main()# Вызов функции main