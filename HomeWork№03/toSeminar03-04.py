#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#*Пример:*
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

import os

def main():
    os.system('CLS')
    number =number_enter()#Введенное число
    trans_dec_auto(number)#Преобразованное введенное число в двоичное встроенной функцией bin
    trans_dec_manual(number)#Преобразованное введенное число в двоичное написанным алгоритмом

def number_enter() -> int:#Ввод числа
    number = int(input('Введите число : '))
    return number

def trans_dec_auto(number : int) -> bin:#Преобразование введенного числа в двоичное встроенной функцией bin:
    number_bin_auto = bin(number)
    print(f'\nЧисло {number} преобразованое в двоичное встроенной функцией bin: {number_bin_auto}')
    
def trans_dec_manual(number : int) -> str:#Преобразование введенного числа в двоичное написанным алгоритмом:
    number_bin_manual = ''
    temp = number
    while temp > 0:
        number_bin_manual = str(temp % 2) + number_bin_manual
        temp = temp // 2
    number_bin_manual ='0b' + number_bin_manual  
    print(f'Число {number} преобразованое в двоичное написанным алгоритмом : {number_bin_manual}\n')

main()#Вызов функции main
