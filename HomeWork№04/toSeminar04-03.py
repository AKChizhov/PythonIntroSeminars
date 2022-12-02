# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
import random

def main():
    os.system('CLS')
    listing_of_number = fill_enter_numbers() # Исходный список из 20 чисел значением от 10 по 20 - для наглядности
    listing_of_number_unic = listing_of_number.copy() # Копия исхоного списка
    fill_numbers_unic(listing_of_number_unic)
    
def fill_enter_numbers() -> list[int]: # Заполняем исходный список 20 генерируемыми числами значением от 10 по 20 
    listing = [] 
    for i in range(0,20):
        temp = random.randint(10 ,20)
        listing.append(temp)
    print(f'\nИсходный список\n{listing}') 
    return listing 
    
def fill_numbers_unic(listing : list[int]) -> list[int]: # Заполняем список уникальными числами из исходного списка
    i = 0
    while(i < len(listing)):
        j = i + 1 
        while(j < len(listing)):
            if(listing[i] == listing[j]): del listing[j]
            else : j +=1
        i +=1
    print(f'Список из уникальных чисел исходного списка\n{listing}\n')             
       
main()