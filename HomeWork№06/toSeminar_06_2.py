#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
import random

def main():
    os.system('CLS')
    list_nu = fill_list () # Сгенерированный список
    summa_od = number_list_odds (list_nu) #  Сумма элементов исходного списка, стоящих на нечётной позиции.
    print(f'   Сумма чисел c нечетными порядковыми номерами из исходного списка равна : {summa_od}\n')
    
def fill_list() -> list[int] : # Генерация исходного списка
    list1 = [random.randint(1,11) for i in range(1,random.randint(5,9))]
    print(f'\n\nИсходный сгенерированный список : {list1}')
    return list1
    
def number_list_odds (list1 : list[int]) -> int: # Вычисление суммы элементов исходного списка, стоящих на нечётной позиции.
    summa = 0
    for id, val  in enumerate(list1):
        if(id % 2 !=0): 
            print(f'Порядковый номер (нечетный индекс списка) элемента списка : {id} его значение : {val}')
            summa = summa + val
    return summa
        
main() # Вызов функции main
