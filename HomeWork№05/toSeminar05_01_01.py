#Создайте программу для игры с конфетами бот  против бота.
# Условие задачи: 
#      На столе лежит 2021 конфета. Играют два бота, делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#      За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

import os
import random

number_of_candies = 2021
players = ['Qwe_BOT', 'Zxc_BOT']

def main ():
    os.system('CLS')
    the_who =  who_fierst() # Кто делает первый ход
    who_end = move(the_who, players) # Кто делает последний ход
    print_message(players[the_who], players[who_end])
    
def who_fierst() -> int: # определение игрока делающего 1-ый ход
    who = random.randint(0,1)
    if(who == 0): print(f'Первым забирает конфеты  {players[who]}')
    else: print(f'Первым забирает конфеты {players[who]}')
    return who
 
def move( nn : int, list1 : list[str]) -> int: # Игра и определение победителя
    candies = number_of_candies
    i = 1
    while(candies > 0):
        j =0
        while(j <= 1):
            if(candies == 0) : break
            elif(candies > 28): frontir = 28
            else: frontir = candies 
            temp = random.randint(1,frontir)
            print(f'Ход № {i} игрока {list1[nn - j]} - он взял конфет :','%2d' % (temp) ,' шт. На столе осталось конфет :','%3d' % (candies - temp),' шт')
            candies = candies - temp
            j +=1
        i+=1
    return (nn - j +1 )
    
def print_message(nnn1,nnn2): # Вывод результатов игры
    print(f'\nИгра закончена. На столе было : {number_of_candies} конфет. Игроки по-очереди брали конфеты,не больше 28 шт.\n'+
        f'Выигрывает забирающий последние конфеты. Игрок {nnn1} начал игру. Игрок {nnn2} победил, ВСЕ конфеты его !!! \n')
             
main()   
