from wonderwords import RandomWord
from data import intro, roundone, introtwo, roundtwo, survivor_needs, maps
from inputimeout import inputimeout, TimeoutOccurred
import os
import keyboard as key
import random as rd
import time
import msvcrt
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
undead = 10
vltl = 20
heal = 20
chaseattempt = 0
attackattempts = 0

def typewriter(text, delay):
    for char in text:
        sys.stdout.write(char)   
        sys.stdout.flush()       
        time.sleep(delay)
    print()

def healop():
    global healopportunity
    global truemove
    if truemove >= 3:
        healopportunity += 1
        truemove = 0
    else:
        healopportunity = healopportunity

def healing():
    global hp
    global healopportunity
    global heal
    yn = input('Do you want to heal? (y/n): ')
    if yn == 'y':
        if healopportunity > 0:
                hp += heal
                healopportunity -= 1
                typewriter(f"Healed, Current HP: {hp}", 0.01)
        else:
            print('No heal opportunity available (need 3 succesful dodges)')
    else:
        print('You chose not to heal')

def attack(x):
    global hp
    global vltl
    global undead
    global truemove
    if x == 'vltl':
        hp -= vltl
    else:
        hp -= 10

    if hp > 0 and x == 'vltl':
        typewriter(f"Attacked by volatile, Current HP: {hp}", 0.05)
    elif hp > 0 and x =='undead':
        typewriter(f"Attacked by undead, Current HP: {hp}", 0.05)
    else:
        print('idk how but you died, you lose')

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    



def clearinput():
    while msvcrt.kbhit():   
        msvcrt.getch()  

def loots():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in nested_map:
        print("".join(row))
    clearinput()
    category = rd.choice(list(survivor_needs.keys()))
    count = rd.randint(1, len(survivor_needs[category]))
    items = rd.sample(survivor_needs[category], count)
    print(f'you found a loot, it contains {items}')
    getpass.getpass('press enter to continue')  
    return items

clearinput()
intro = (getpass.getpass('                 Press enter to start the game'))
os.system('cls' if os.name == 'nt' else 'clear')

for i in roundone:
    print(i)
    time.sleep(0.1)
time.sleep(2)
print(' ')

while chaseattempt <= 1:
    r = RandomWord()
    word = r.word(word_min_length=10, word_max_length=20)
    print(f'Input the word: {word} (5 secs)')
    inputword = []
    try:
        userinput = inputimeout(prompt='> ', timeout=5)
        inputword.append(userinput)
        inputwordcapital = inputword[0].upper()
    except TimeoutOccurred:
        inputword.append(None)

    if inputword[0] is not None:
        if inputword[0] == word or inputwordcapital == word.upper():
            truemove += 1
            chaseattempt += 1
            typewriter("you dodged the attack", 0.1)
            time.sleep(1)
            clearinput()
            if healopportunity >= 1 and hp < 100:
                healop()
                healing()
            else:
                healop()
        else:
            chaseattempt += 1
            print("Wrong word mate, you got hit")
            attack('vltl')
            clearinput()
            time.sleep(1)
    else:
        chaseattempt += 1
        print("Time's up mate, you got hit")  
        attack('vltl')
        clearinput()
        time.sleep(1)

if chaseattempt >= 1:
    print('youve passed the night, you win!')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')


for i in introtwo:
    print(i)
    time.sleep(0.1)

time.sleep(2)
print('..............................................................')
print('....   your people need some stuffs in order to survive   ....')
print('....     but that stuffs only available in dark zone      ....')
print('....     youre the only capable person for this task      ....')
print('....                                                      ....')
time.sleep(2)
print('....                 YOU ARE A SCAVENGER                  ....')
print('....   YOU WILL GATHER ALL THE STUFFS FOR THE SURVIVORS   ....')
print('....                USE ARROW KEYS TO MOVE                ....')
print('....                USE E KEY TO INTERACT                 ....')
print('..............................................................')
print('..............................................................')
print('..............................................................')
clearinput()
intro = (getpass.getpass('                 Press enter to start the game'))
os.system('cls' if os.name == 'nt' else 'clear')

for i in roundtwo:
    print(i)
    time.sleep(0.1)
time.sleep(2)
print('')

class stuffs:
    def __init__(self, weapon, consumable, craftingpart, rareitem):
        self.weapon = weapon
        self.consumable = consumable
        self.craftingpart = craftingpart
        self.rareitem = rareitem

    def wantedstuffs(self):
        wantedweapon = rd.choice(survivor_needs["weapons"])
        wantedconsumable = rd.choice(survivor_needs["consumables"])
        wantedcraftingpart = rd.choice(survivor_needs["crafting_parts"])
        wantedrareitem = rd.choice(survivor_needs["rareitems"])

game_map = rd.choice(list(maps.values()))
nested_map = [list(row) for row in game_map]


player_y, player_x = 0, 0
for y, row in enumerate(nested_map):
    for x, char in enumerate(row):
        if char == '😎':
            player_y, player_x = y, x
            break



while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in nested_map:
        print("".join(row))
    pressed_input = key.read_event()
    if pressed_input.event_type == key.KEY_DOWN:
        new_x, new_y = player_x, player_y    
        if pressed_input.name == 'up':      
            new_y -= 1
        elif pressed_input.name == 'down':  
            new_y += 1
        elif pressed_input.name == 'left':  
            new_x -= 1
        elif pressed_input.name == 'right': 
            new_x += 1
        elif pressed_input.name == 'esc':
            break

        if 0 <= new_y < len(nested_map) and 0 <= new_x < len(nested_map[0]):
            target_cell = nested_map[new_y][new_x]
            if target_cell == '💀':
                print('')
                print('kill the undead')
                time.sleep(2)
                while attackattempts <= 4:
                    r = RandomWord()
                    word = r.word(word_min_length=10, word_max_length=20)
                    print(f'Input the word: {word} (5 secs)')
                    inputword = []
                    try:
                        clearinput()
                        userinput = inputimeout(prompt='> ', timeout=5)
                        inputword.append(userinput)
                        inputwordcapital = inputword[0].upper()
                    except TimeoutOccurred:
                        inputword.append(None)
                    except Exception:
                        inputword.append(None)

                    if inputword[0] is not None:
                        if inputword[0] == word or inputwordcapital == word.upper():
                            truemove += 1
                            attackattempts += 1
                            typewriter("you slashed the undead", 0.01)
                            time.sleep(1)
                            if healopportunity >= 1 and hp < 100:
                                healop()
                                healing()
                            else:
                                healop()
                        else:
                            attackattempts += 1
                            print("Wrong word mate, you got bitten")
                            attack('undead')
                            time.sleep(1)
                    else:
                        attackattempts += 1
                        print("Time's up mate, you got bitten")  
                        attack('undead')
                        time.sleep(1)
                attackattempts = 0        
                nested_map[player_y][player_x] = '⬜' 
                player_x, player_y = new_x, new_y
                nested_map[player_y][player_x] = '😎'  

            elif target_cell == '👿': 
                os.system('cls' if os.name == 'nt' else 'clear')
                typewriter('you bumped a volatile and trapped in the dark zone', 0.05)
                time.sleep(0.5)
                typewriter('            you cant fight against it             ', 0.05)
                time.sleep(0.5)
                typewriter('         meet your doom in the dark zone          ', 0.05)
                sys.exit()

            elif target_cell == '📦':
                nested_map[player_y][player_x] = '⬜' 
                player_x, player_y = new_x, new_y
                nested_map[player_y][player_x] = '😎'
                loots()    

            elif target_cell != '⬛':
                nested_map[player_y][player_x] = '⬜' 
                player_x, player_y = new_x, new_y
                nested_map[player_y][player_x] = '😎'
                
    time.sleep(0.05)
    

        
