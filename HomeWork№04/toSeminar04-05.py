#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
#В file1.txt :
#             2*x**2 + 4*x + 5
#В file2.txt:
#             4*x**2 + 1*x + 4
#Результирующий файл:
#             6*x**2 + 5*x + 9

#(ord('0'))# 48
#(ord('9'))# 57
import os
os.system('CLS')

FILENAME1 = "file1.txt"
FILENAME2 = "file2.txt"

with open(FILENAME1, "r") as file:
    for polynomial in file:
        print(polynomial, end="")
print('\n')
     
polynomial = polynomial.split(" + ")
list_of_koeff = []
i = 0
while(i < len(polynomial)):
    temp = ""
    for char in polynomial[i]:
        if(ord(char) >= 47 and ord(char) <= 57):
            temp = str(temp) + str(char)
            #print(temp)
        else : break 
    i+=1  
    list_of_koeff.append(temp)  
print('\n',polynomial)
print('\n',list_of_koeff)
