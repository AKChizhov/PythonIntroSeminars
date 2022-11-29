#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
#*Пример:*
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
#Нужно распространить на отрицательные числа? Вместо f(n)=f(n-2)+f(n-1) используем f(n)=f(n+2)-f(n+1) и идём "сверху вниз":

import os

def main():
    os.system('CLS')
    number =number_enter()#Введенное число
    os.system('CLS')
    print_message()
    fibonacci(number)
    
def number_enter() -> int:#Ввод числа
    number = int(input('Введите число : '))
    return number

def print_message():
    print('Для отрицательных чисел Фибоначчи вместо f(n)=f(n-2)+f(n-1) используем f(n)=f(n+2)-f(n+1)')

def fibonacci(number : int):
    fibonacci1 = [0,1]
    i = 2
    while(i <= number):
        temp1 = fibonacci1[i - 1] + fibonacci1[i - 2]
        fibonacci1.append(temp1)
        i +=1
    
    fibonacci2 = [0,1]
    j = 2
    while(j <= number):
        temp2 = fibonacci2[j - 2] - fibonacci2[j - 1]
        fibonacci2.append(temp2)
        j +=1
    fibonacci2.reverse()
    
    k = 1
    while(k <= number):
        fibonacci2.append(fibonacci1[k])
        k +=1
    print(f'\nРяд Фибоначчи для чисел от {number} по {-number}\n {fibonacci2}\n')
    
main()