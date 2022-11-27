#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Для продвинутых - с файлом ( вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
import os
os.system('CLS')

FILENAME = "dataTo04.txt"#Название файла
messages = list()#Сщоздан пустой список
 
number = int(input('Введите число N : ') ) 
for i in range(-number,  (number + 1)):
    message = str(int(i))
    messages.append(message + '\n')

# запись списка в файл
with open(FILENAME, "w") as file:
    for message in messages:
        file.write(message)
print(message, end='')
print(f'Список из элементов, заполненных числами из промежутка от : {-number} по: {number} записан в файл {FILENAME}')
 
# считываем сообщения из файла
dat = []
with open(FILENAME, "r") as file:
    i=0
    for message in file:
        dat.append(int(message))
print(dat)
print(f'Список из элементов, заполненных числами из промежутка от : {-number} по: {number} считан из  файла {FILENAME}')

mult = 1
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
    if(borders[i] < -number or borders[i] > number):
         myFlag = 0  
    i+=1    

if(myFlag == 1):
    j = 0
    while(j < len(dat)):
        if(dat[j] == borders[0]): 
            jStart = j 
        if(dat[j] == borders[1]): 
            jEnd = j
        j+=1 
            
    mult = 1
    i = jStart
    while (i  <= jEnd):
        if(dat[i] != 0): mult = mult * dat[i]
        i += 1
    print(f'\nПроизведение чисел от : {borders[0]}  по: {borders[1]} ( 0 не учитывается ) равно : {mult}\n')
else:
    print('\nНеправильный ввод') 