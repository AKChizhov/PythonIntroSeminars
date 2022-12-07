# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)

import os
 
def main():
    pole = list(map(str,range(1,82))) # Игровое поле 9 на 9 из чисел от 1 по 81
    the_aim = sum(range(1,82)) / 81 # Среднее значение списка из чисел от 1 по 81
    i = 0 
    while(i < 5): # Для наглядности игроки забирают по 5 чисел
        os.system('CLS')
        pole_print(pole)
        pole = move_on_pole('X', pole)
        os.system('CLS')
        pole_print(pole)
        pole = move_on_pole('O', pole)
        pole_print(pole)
        i +=1
    find_victory(pole, the_aim) 
      
def pole_print(list1 : list[str]): # Вывод игрового поля
    i = j = k = 0
    print('─' * 44)
    while (i < 9):
        while (j < 9):
            print('%2s' % list1[k], end=" │ ")
            k += 1
            j += 1
        print('\n','─' * 43)
        j = 0
        i += 1

def move_on_pole(what, list1): # Заполнение игроками своих списков
    pos  = str(input(f'Куда поставим {what} ? - задайте число из имеющихся на поле.( Для выхода - любая клавиша)  '))
    if(pos ==''): exit() # Выход из программы
    else :
        pos = str(pos)
        temp1 = int(pos)
    if(temp1 > 81  or temp1 < 1) : move_on_pole(what, list1) # Проверка правильности ввода и повторный ввод
    else :
        temp = list1.index(pos)
        list1[temp] = what
    return list1

def find_victory(list1 : list[str], target : float): # Определение победителя
    list_of_O = []
    list_of_X = []
    i = 0
    while(i < len(list1)):
        if(list1[i] == 'O'): list_of_O.append(i + 1)
        elif(list1[i] == 'X'): list_of_X.append(i + 1)
        i+=1
    average_of_list_of_O = sum(list_of_O) / len(list_of_O) # Среднее значение списка игрока О
    delta_0 = abs(target - average_of_list_of_O)
    print(f'Список игрока O: {list_of_O} Цель: {target} Среднее значение списка O : {round(average_of_list_of_O,2)}'+
          f' Отклонение:  {round(delta_0,2)}')
    average_of_list_of_X = sum(list_of_X) / len(list_of_X) # Среднее значение списка игрока Х
    delta_X = abs(target - average_of_list_of_X)
    print(f'Список игрока Х: {list_of_X} Цель: {target} Среднее значение списка X : {round(average_of_list_of_X,2)}'+
          f' Отклонение:  {round(delta_X,2)}')
    print(f'Среднее значение чисел в списке от 1 по 81 : {target}, задача составить свой список такими числами,\n'+
          f'чтобы их среднее значение было как можно "ближе" к {target} чем у второго игрока. Ставят по 5 чисел.' )
    if(delta_0 < delta_X): print('Победил игрок O\n')
    else : print('Победил игрок X\n')  
    
main()


