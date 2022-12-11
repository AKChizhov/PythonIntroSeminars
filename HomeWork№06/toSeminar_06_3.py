#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Для продвинутых - с файлом ( вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
import os
os.system('CLS')

FILENAME = "dataTo06.txt"#Название файла
ourDates = list()#Создан пустой список
 
number = int(input('Введите число N : ') ) 
for i in range(-number,  (number + 1)):
    ourDates.append(str(int(i)) + '\n')

with open(FILENAME, "w") as file: # запись списка в файл
    for ourData in ourDates:
        file.write(ourData)
print(ourData, end='')
print(f'Список из элементов, заполненных числами из промежутка от : {-number} по: {number} записан в файл {FILENAME}')
 
dat = []
with open(FILENAME, "r") as file: # считываем список из файла
    i=0
    for ourData in file:
        dat.append(int(ourData))
print(dat)
print(f'Список из элементов, заполненных числами из промежутка от : {-number} по: {number} считан из  файла {FILENAME}')

mult = 1 #Вычисление проиведения всех считанных чисел
i = 0
while (i < len(dat)):
    if(dat[i] != 0):
        mult = mult * dat[i]
    i+= 1
print(f'\nПроизведение чисел от : {-number}  по: {number} ( 0 не учитывается ) равно : {mult}\n')

print(f'Введите через пробелы или запятую  2 числа из выше указанного интервала от  {-number}  по: {number}')
borders = input()
borders = borders.replace(',', '')
borders = list(map(int,borders.split()))
i = 0
myFlag = 1
while( i < 2):
    if(borders[i] < -number or borders[i] > number ):#Проверка правильности ввода
        myFlag = 0  
    i+=1    

if(myFlag == 1):#определение индексов выбранного интервала
    j = 0
    while(j < len(dat)):
        if(dat[j] == borders[0]):  jStart = j 
        if(dat[j] == borders[1]):  jEnd = j
        j+=1 
    
    mult = 1
    for i in dat[jStart : jEnd +1] :
        if ( i != 0): 
            mult = mult * i
    print(dat[jStart : jEnd +1])       
    print(f'\nПроизведение чисел от : {borders[0]}  по: {borders[1]} ( 0 не учитывается ) равно : {mult}\n')
else:
    print('\nНеправильный ввод')
    