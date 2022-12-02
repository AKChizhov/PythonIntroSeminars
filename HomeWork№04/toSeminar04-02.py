#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 6 -> [1,2,3]
# 144 -> [2,3]

import os

def main():
    os.system('CLS')
    my_number = enter_number()
    my_list_of_factors = list_of_factors(my_number)
    
def enter_number()  -> int:
    number = int(input('Введите число :'))   
    print(f'Введено число : {number}') 
    return number

def list_of_factors(number : int) -> list[int]:
    listing = []
    for i in range(1,number + 1):
        temp = number % i
        if(temp == 0 ): listing.append(i)   
    #print(listing)  

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
    print(f'Список простых множителей введенного числа {number} : {listing_result}\n')
     
main()