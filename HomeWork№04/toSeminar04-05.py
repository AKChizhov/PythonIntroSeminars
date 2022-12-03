#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
#В file1.txt :
#             2*x**2 + 4*x + 5
#В file2.txt:
#             4*x**2 + 1*x + 4
#Результирующий файл:
#             6*x**2 + 5*x + 9


#(ord('0')) = 48
#(ord('9')) = 57

import os

FILENAME1 = "file1.txt" # 1-й файл с исходными данными
FILENAME2 = "file2.txt" # 2-й файл с исходными данными
FILENAME = "file3.txt" # файл с результатом

def main():
    os.system('CLS')
    polynomial_1 = open_file(FILENAME1) # строка из 1-го файла
    polynomial_2 = open_file(FILENAME2) # строка из 2-го файла
    list_of_koeff_1 = create_koeff(polynomial_1) # список коэфф. из 1-го файла
    list_of_koeff_2 = create_koeff(polynomial_2) # список коэфф. из 2-го файла
    list_of_koeff_summ = summ_koeff(list_of_koeff_1 , list_of_koeff_2)#список сумм коэфф.из обоих файлов
    polynomial_out = create_polynomial(list_of_koeff_summ) # искомый многочлен ( строка )
    print_into_fail(polynomial_out) 

def open_file(FILENAME): # считывание информации из файла
    with open(FILENAME, "r") as file:
        for polynomial in file:
            print(polynomial, end="")
    print('\n')
    return polynomial
    
def create_koeff(polynomial : str) -> list[int]: # создание списка коэфф. многочлена     
    polynomial = polynomial.split(" + ")
    list_of_koeff = []
    i = 0
    while(i < len(polynomial)):
        temp = ""
        for char in polynomial[i]:
            if(ord(char) >= 47 and ord(char) <= 57):
             temp = str(temp) + str(char)
            else : break 
        i+=1  
        list_of_koeff.append(temp)  
    print(f'Список коэфф. из файла : {list_of_koeff}')
    return list(map(int,list_of_koeff))

def summ_koeff(list_1 : list[int],list_2 : list[int] ) -> list[str]: #суммируем коэфф.
    i = 0
    list_3 = []
    while(i < len(list_1)):
        temp = list_1[i] + list_2[i]
        list_3.append(temp)
        i+=1
    list_3 = list(map(str,list_3))
    print(f'Список сумм коэфф. из файла : {list_3}')
    return list_3
       
def create_polynomial(coeffs :list[str]): # Формирование многочлена
    polynomial = []    
    j = 0
    number = len(coeffs)
    while(j<number - 1):
        temp1 = f"{coeffs[j]}*X**{number - 1 - j} + "     
        polynomial.append(temp1)   
        j+=1
    temp2 = f"{coeffs[number - 1]} = 0"
    polynomial.append(temp2)             
    k = 1
    result = polynomial[0]
    while (k < number):
        result = result + polynomial[k]
        k+=1
    print(f'Сформирован многочлен  : {result} ,\nзаписанный также в файл {FILENAME} \n')
    return result    
    
def print_into_fail(result): # запись многочлена в файл
    with open(FILENAME, "w") as file:     
        file.write(result)
    
main()