#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
import random
import math
import os
os.system('CLS')
a=list()
i=0
while i < 4:
    d = round((random.random() *100-49),1)
    a.append(d)
    i+=1
print(f'\n\tКоординаты точек сгенерированы \n\n\t {a}')
#a=[3, 6, 2, 1]  #использовался для проверки, результат 5,1
#a=[7, -5, 1, -1] #использовался для проверки, результат 7,2
print(f'\n\tКоординаты точки А ({a[0]},{a[1]})')
print(f'\n\tКоординаты точки B ({a[2]},{a[3]})')
print(f'\n\tPасстояние между ними : {round(math.sqrt((a[2]-a[0])**2+(a[3]-a[1])**2),1)}\n')#длинно и неудобно