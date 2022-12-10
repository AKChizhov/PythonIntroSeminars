#Создайте программу для игры с конфетами бот  против бота.
# Условие задачи: 
#      На столе лежит 117 конфета. Играют два бота, делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#      За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# !!! Примечание !!! Программа упрощена относительно сданной к семинару №5 и реальзован вывод методом ZIP - списков

import os
import random

index = [] # Список №№ ходов игроков (ботов)
candies_on_table_pre = [] # Список кол-ва конфет до хода
candies_on_table_aft = [] # Список кол-ва конфет после хода
who_index = [] # Список последовательности ходов игроков (ботов) 

number_of_candies = 117 # Начальное кол-во конфет на столе
players = ['Qwe_BOT', 'Zxc_BOT'] #

def main ():
    os.system('CLS')
    the_who =  who_fierst() # Кто делает первый ход
    who_end = move(the_who, players) # Кто делает последний ход
    print_play(index,candies_on_table_pre,who_index,candies_on_table_aft) # Вывод ходов игроков (ботов)
    print_message(players[the_who], players[who_end]) # Вывод результатов игры
    
def who_fierst() -> int: # определение игрока делающего 1-ый ход
    return random.randint(0,1)

def move( nn : int, list1 : list[str]) -> int: # Игра и определение победителя
    candies = number_of_candies
    i = 1
    while(candies > 0):
        j =0
        while(j <= 1):
            candies_on_table_pre.append(candies)
            if(candies == 0) : break
            if(candies <= 28) :
                candies = 0
            else : 
                temp = random.randint(1,28)
                candies = candies - temp
            index.append(i)    
            who_index.append(list1[nn - j])
            candies_on_table_aft.append(candies)
            j +=1
        i+=1
    return(nn - j + 1)
    
def print_play(index,candies_on_table_pre,who_index,candies_on_table_aft) : # Вывод ходов игроков (ботов)  
    print('\n\n')
    for index,candies_on_table_pre,who_index,candies_on_table_aft in zip(index,candies_on_table_pre,who_index,candies_on_table_aft):
        print('Ход №','%2d' %index,' конфет на столе было :','%4d'% candies_on_table_pre, ' игрок ',who_index, ' взял конфет :'+
              '%3d' % (candies_on_table_pre - candies_on_table_aft), ' Конфет осталось :','%4d'% candies_on_table_aft) 
    
def print_message(nnn1,nnn2): # Вывод результатов игры
    print(f'\nИгра закончена. На столе было : {number_of_candies} конфет. Игроки по-очереди брали конфеты,не больше 28 шт.\n'+
        f'Выигрывает забирающий последние конфеты. Игрок {nnn1} начал игру. Игрок {nnn2} победил, ВСЕ конфеты его !!! \n')
             
main()   
