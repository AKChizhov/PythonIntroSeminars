#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Для продвинутых - с файлом ( вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
import os
number = int(input('Введите число N : ') )
#numberMap = list(map(int ,range( -number,  (number + 1))))
numberMap = range( -number,  (number + 1))
numberList = []
for i in numberMap:
    numberList.append(int( numberMap[i] ))
numberList.sort()
try:
    somefile = open("dataTo04.txt", "w")
    try:
        #somefile.write("hello Sasha !")
        with open('dataTo04.txt', 'a') as file:
            print(numberList, file=file )  
        somefile.write("hello Sasha !")     
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)

os.system('type dataTo04.txt')
