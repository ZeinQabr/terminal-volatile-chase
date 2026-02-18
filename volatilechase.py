from wonderwords import RandomWord
from data import intro, roundone
import threading
import time
import getpass
import sys

for i in intro:
    print(i)
    time.sleep(0.1)
    
time.sleep(2)
print('##############  youve been chasing by volatiles ###############')
print('##############           save yourself!         ###############')
time.sleep(2)
print('##############                                  ###############')
print('############## insert with the correct input to ###############')
print('##############        escape volatiles!         ###############')
print('##############                                  ###############')
print('##############                                  ###############')
print('##############                                  ###############')
print('##############                                  ###############')
print('###############################################################')

truemove = 0
healopportunity = 0
hp = 100
vltl = 20
heal = 20
chaseattempt = 0

def healop():
    global healopportunity
    global truemove
    if truemove >= 3:
        healopportunity += 1
    else:
        healopportunity = 0

def healing():
    global hp
    global healopportunity
    global heal
    yn = input('Do you want to heal? (y/n): ')
    if yn == 'y':
        if healopportunity > 0:
                hp += heal
                healopportunity -= 1
                print(f"Healed, Current HP: {hp}")
        else:
            print('No heal opportunity available (need 3 succesful dodges)')
    else:
        print('You chose not to heal')

def attack():
    global hp
    global vltl
    global truemove
    truemove -= 1
    hp -= vltl
    if hp > 0:
        print(f"Attacked by volatile, Current HP: {hp}")
    else:
        print('you died')
        sys.exit()

intro = (getpass.getpass('                 Press enter to start the game'))

for i in roundone:
    print(i)
    time.sleep(0.1)
time.sleep(2)

while chaseattempt <= 10:
    r = RandomWord()
    word = r.word(word_min_length=10, word_max_length=20)
    print(f'Input the word: {word} (10 detik)')
    inputword = []
    inputword.append(input('> '))

    if inputword:
        if inputword[0] == word:
            truemove += 1
            chaseattempt += 1
            print("you dodged the attack")
            if healopportunity >= 1 and hp < 100:
                healop()
                healing()
            else:
                healop()
        else:
            chaseattempt += 1
            print("Wrong word mate, you got hit")
            attack()
    else:
        chaseattempt += 1
        print("Time's up mate, you got hit")  
        attack()          
if chaseattempt >= 10:
    print('youve passed the night, you win!')
        
        





