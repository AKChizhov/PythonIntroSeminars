#Реализуйте алгоритм перемешивания списка.
import os
os.system('CLS')
import random 
listA = [] 
i=0
while (i < 10):
    d = random.randint(10, 20)
    listA.append(d)
    i+=1
print(listA)  
print('\nВыше список из 10 сгенерированных чисел чисел. Ниже 10 списков перемешанных методом shuffle\n')
i =0
while (i < 10):
    random.shuffle(listA)
    print(listA)
    i+=1
print('\n')