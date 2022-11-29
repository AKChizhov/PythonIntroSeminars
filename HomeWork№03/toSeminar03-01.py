#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
import random

def main():
    os.system('CLS')
    volume = create_volume()
    list1 = fill_list (volume)
    list2 = number_list_odds (list1)
    print(f'Сумма нечетных чисел {list2} из исходного списка равна : {sum_odds(list2)}\n')
    
def create_volume():
    volume = random.randint(3,9)
    return volume

def fill_list(volume : int ):
    listOfNumbers = []
    i = 0
    while( i < volume):
        temp = random.randint(1,10)
        listOfNumbers.append(temp) 
        i+=1
    print(f'\nИсходный сгенерированный список : {listOfNumbers}')
    return listOfNumbers
    
def number_list_odds (list1 : list):
    list2 = []
    i = 1
    ii = len(list1)
    while(i < ii):
        list2.append(list1[i])
        i+=2
    return list2

def sum_odds (list2 : list):
    summa = sum(list2)
    return(summa)
        
main()# Вызов функции main
