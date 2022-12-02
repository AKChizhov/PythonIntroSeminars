#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
#Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0

import os
import random

def main():
    os.system('CLS')
    my_degree = enter_degree()
    fill_coefficients(my_degree)
    
        
def enter_degree() -> int: 
    number = int(input('Введите степень  К  многочлена :')) 
    return number
    
def fill_coefficients(number : int) -> str:
    coeffs = []
    i = 0
    while(i <= number):
        temp = random.randint(0,100)
        coeffs.append(temp)
        i+=1
    print(coeffs)
     
    polynomial = []    
    j = 0
    while(j<number):
        temp1 = f"{coeffs[j]}*X**{number - j} + "     
        polynomial.append(temp1)   
        j+=1
    temp2 = f"{coeffs[number]} = 0"
    polynomial.append(temp2)    
             
    print(polynomial)
    k = 1
    result = polynomial[0]
    while (k <= number):
        result = result + polynomial[k]
        k+=1
    print(result)
    with open("hello.txt", "w") as file: # запись списка в файл      
         file.write(result)
    return polynomial
     
main()