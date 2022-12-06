#Создайте программу для игры с конфетами человек против бота.
# Условие задачи: 
#      На столе лежит 117 конфета. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#      За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

import os
import random

number_of_candies = 117
players = ['Бот ', 'Человек']

def main ():
    os.system('CLS')
    the_who =  who_fierst() # Кто делает первый ход
    who_end = move(the_who, players) # Кто делает последний ход
    print_message(players[the_who], players[who_end]) #
    
def who_fierst() -> int: # определение игрока делающего 1-ый ход
    who = random.randint(0,1)
    if(who == 0): print(f'Первым забирает конфеты  {players[who]}')
    else: print(f'Первым забирает конфеты {players[who]}')
    return who 
       
def move( nn : int, list1 : list[str]) -> int: # Игра и определение победителя
    candies = number_of_candies
    i = 1
    while(candies > 0):
        if(nn ==0):
            if(candies == 0) : break
            elif(candies >= 28) : frontir = 28
            else: frontir = candies
            temp = random.randint(1,frontir)
            k = 0
            print((f'Ход {i} Игрока {list1[0]}, на столе конфет {candies} , он взял конфет : {temp}' ))
            candies = candies - temp
            if(candies == 0) : break
            temp = int (input((f'Ход {i} Игрока {list1[1]}, на столе конфет {candies} , сколько возмете ? ' )))
            k = 1
            candies = candies - temp
        else :
            temp = int (input((f'Ход {i} Игрока {list1[1]}, на столе конфет {candies} , сколько возмете ? ' )))
            k = 1
            candies = candies - temp
            if(candies == 0) : break
            elif(candies >= 28) : frontir = 28
            else: frontir = candies
            temp = random.randint(1,frontir)
            k = 0
            print((f'Ход {i} Игрока {list1[0]}, на столе конфет {candies} , он взял конфет : {temp}' ))
            candies = candies - temp
    i+=1
    return k
 
def print_message(nnn1 : int, nnn2 : int): # Вывод результатов игры
    print(f'\nИгра закончена. На столе было : {number_of_candies} конфет. Игроки по-очереди брали конфеты,не больше 28 шт.\n'+
        f'Выигрывает забирающий последние конфеты. Игрок {nnn1} начал игру. Игрок {nnn2} победил, ВСЕ конфеты его !!! \n') 
 
main()   
