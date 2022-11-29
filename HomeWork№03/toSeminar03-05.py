#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
#*Пример:*
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

import os

def main():
    os.system('CLS')
    number =number_enter()#Введенное число
    os.system('CLS')
    print_message()#Сообщение об особенности вычисления отрицательных чисел Фибоначчи
    fibonacci(number)
    
def number_enter() -> int:#Ввод числа
    number = int(input('Введите число : '))
    return number

def print_message():
    print('Для отрицательных чисел Фибоначчи вместо f(n)=f(n-2)+f(n-1) используем f(n)=f(n+2)-f(n+1)')

def fibonacci(number : int):
    fibonacci1 = [0,1] #Список для положительных чисел Фибоначчи 
    fibonacci2 = [0,1] #Список для отрицательных чисел Фибоначчи
    i = 2
    while(i <= number):
        temp1 = fibonacci1[i - 1] + fibonacci1[i - 2]
        temp2 = fibonacci2[i - 2] - fibonacci2[i - 1]
        fibonacci1.append(temp1)
        fibonacci2.append(temp2)
        i +=1
    
    fibonacci2.reverse()#Реверс списка с отрицательными числами Фибоначчи
    
    k = 1
    while(k <= number):
        fibonacci2.append(fibonacci1[k])#Объединение списков отриц. и полож. чисел Фибоначчи
        k +=1
    print(f'\nРяд Фибоначчи для чисел от {number} по {-number}\n {fibonacci2}\n')
    
main()#Вызов функции main