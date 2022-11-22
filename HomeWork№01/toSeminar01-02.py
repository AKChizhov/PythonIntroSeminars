#   Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#   Где: ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

import os
os.system('CLS')
print('Введите через пробелы или запятую числа X,Y,Z')
xyz = input()
xyz=xyz.replace(',', ' ')# resplit не заработал, все исключения обработать не удалось
xyz = list(map(float,xyz.split()))
print(xyz)
i=0
while i < len(xyz):
    print(xyz[i], end=' ')
    i+=1
leftSide = not (xyz[0] or xyz[1] or xyz[2])#¬(X ⋁ Y ⋁ Z)
rightSide = not xyz[0] and not xyz[1] and not xyz[2]#¬X ⋀ ¬Y ⋀ ¬Z
#print('\n',not (xyz[0] or xyz[1] or xyz[2]) == not xyz[0] and not xyz[1] and not xyz[2]) - не читаемо, разделил на 2 части
print('\n\tРезультат : ',leftSide == rightSide,'\n')