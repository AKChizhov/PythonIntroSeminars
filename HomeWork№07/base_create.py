
import random
import logger as lg

with open('base_phone.csv', 'w') as file:
    file.writelines("ID,Name,Surname,PhoneNumber,e-mail\n")

name_personal = ['Oliver', 'Jack','Harry' ,'Jacob' ,'Charlie','Thomas', 'Oscar', 'William' ,'James', 'George','Amelia','Olivia', 'Emily', 'Ava', 
                 'Jessica', 'Isabella' ,'Sophie' ,'Mia','Ruby','Lily'] # Библиотека имен, фамилий - ниже.
surname = ['Smith','Johnson','Williams','Jones','Brown','Davis','Miller','Wilson','Moore','Taylor','Anderson','Thomas','Jackson','White','Harris',
           'Martin','Thompson','Wood','Lewis','Scott','Cooper','King','Green','Walker','Edwards','Turner','Morgan','Baker','Hill','Phillips']
ls_e_mail = ['@gmail.com', '@yahoo.com', 'hotmail.com','aol.com'] # Библиотека почтовых доменов

def start():
    with open('base_phone.csv', 'w') as file :
        for i in range(1,21): # База на 20 персон - для наглядности в учебных целях
            file.write(f'{str(i)},{string_creation()}\n')
 
    lg.logging.info('User create base_phone.csv file')

def list_of_numbers(): # Генерация телефонных номеров (США)
    randomListPhone = random.randint(19010000000, 19090000000)
    s = '+' + str(randomListPhone)
    return s

def string_creation(): # Cоставление строки на каждого человека
    temp1 = random.choice(name_personal) 
    temp2 = random.choice(surname)    
    s = temp1 + ','+  temp2 + ',' + list_of_numbers() + ',' + temp1 + temp2 + str(random.randint(1001,9999)) + random.choice(ls_e_mail)   
    return s

start()