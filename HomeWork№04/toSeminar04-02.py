#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 6 -> [1,2,3]
# 144 -> [2,3]

import os
import time

def main():
    os.system('CLS')
    my_number = enter_number()#Вводимое число
    time.sleep(4)
    os.system('CLS')  
    my_list_of_factors = list_of_factors(my_number)#Список всех множителей числа N
    list_of_simpl_factors(my_number, my_list_of_factors)#Вывод на экран списка простых множителей числа N
    
def enter_number()  -> int:#Ввод числа
    number = int(input('Введите число : '))   
    print(f'Введено число : {number} Думаю....') 
    return number

def list_of_factors(number : int) -> list[int]: #Составление списка всех множителей числа N
    listing = []
    for i in range(1,number + 1):
        temp = number % i
        if(temp == 0 ): listing.append(i)  
    return listing

def list_of_simpl_factors(number : int , listing : list[int]):#Составление списка простых множителей из списка всех множителей числа N
    listing_result = [1]    
    i =  1
    while(i < len(listing)):
        j = 1
        my_flag = 1
        while(j <= i):          
            temp =float( listing[i] / listing[j]) 
            k=1
            while(k <= i):
                if(temp == float(listing[k] )): my_flag = 0
                k+=1
            j+=1
        if(my_flag == 1): listing_result.append(listing[i])
        i+=1
    print(f'\nСписок простых множителей введенного числа {number} : {listing_result}\n')
     
main()