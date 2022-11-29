#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
import random
import math

def main():
    os.system('CLS')
    print_message()
    volume = create_volume()#Число элементов исходного списка
    list1 = fill_list (volume)#Исходный список
    list2 = fill_list_fraction(list1)#Список из значений дробных частей исходного списка
    result(list2)#
    
    
def print_message():
    print('\nБудет сгенерирован список из вещественных чисел от 0 по 100. Кол-во чисел от 3 по 9 - для наглядности.')#Что делаем    
    
def create_volume() -> int:
    volume = random.randint(3,9)#Определяем кол-во элементов списка (для наглядности  от 0 до 100)
    return volume

def fill_list(volume : int ) -> int:
    listOfNumbers = []#Заполняем с помощью генерации исходный список (для наглядности числами от 1 по 9).
    i = 0
    while( i < volume):
        temp = round((random.random() * 100), 2)
        listOfNumbers.append(temp)
        i+=1
    print(f'\nИсходный сгенерированный список : {listOfNumbers}')
    return listOfNumbers

def fill_list_fraction(list1 : float) -> float:#Заполняем список дробными частями элементов исходного списка
    list2 = []
    i = 0
    while(i < len(list1)):
        temp = round(list1[i] - int(list1[i]),2)
        list2.append(temp)
        i += 1
    print(f'Список, составленный из дробных частей элементов исходного списка : {list2}')
    return list2

def result (list2 : float):#Вычисляем разницу между макс и мин значениями дробных частей исходного списка
    delta = round(max(list2) - min(list2),2 )
    print(f'Макс значение дробной части : {max(list2)}, мин значение дробной части : {min(list2)}, их разница : {delta}\n')
 
main()
    