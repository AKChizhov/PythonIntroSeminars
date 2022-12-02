#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
#Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0

import os
import random

FILENAME = "to04.txt"

def main():
    os.system('CLS')
    my_degree = enter_degree()# Степень многочлена
    my_scoefficient = fill_scoefficient(my_degree)# Коэффициенты многочлена
    my_result = create_polynomial(my_scoefficient, my_degree)# Сформированный многочлен
    print_into_fail(my_result)
        
def enter_degree() -> int: # Ввод степени многочлена
    number = int(input('Введите степень  К  многочлена : ')) 
    return number
    
def fill_scoefficient(number : int) -> str: # Генерирование коэффициентов многочлена
    coeffs = []
    i = 0
    while(i <= number):
        temp = random.randint(0,100)
        coeffs.append(temp)
        i+=1
    print(f'\nСформирован список коэффициентов многочлена : {coeffs}')
    return coeffs
     
def create_polynomial(coeffs :list[int] , number : int): # Формирование многочлена
    polynomial = []    
    j = 0
    while(j<number):
        temp1 = f"{coeffs[j]}*X**{number - j} + "     
        polynomial.append(temp1)   
        j+=1
    temp2 = f"{coeffs[number]} = 0"
    polynomial.append(temp2)             
    k = 1
    result = polynomial[0]
    while (k <= number):
        result = result + polynomial[k]
        k+=1
    print(f'Сформирован многочлен степени {number} : {result} ,\n\t записанный также в файл {FILENAME}\n')
    return result

def print_into_fail(result): # запись списка в файл
    with open(FILENAME, "w") as file:     
         file.write(result)
    
main()