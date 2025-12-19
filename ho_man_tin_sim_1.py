#this is the ho man tin sumulation code
import time 
import random
import math
import os 

colors = {
    "C": 39, #default
    "U": 32, #green
    "R": 36, #blue
    "E": 35, #purple
    "L": 33, #yellow
}

rarity = {
    1: "C",
    2: "U",
    3: "R",
    4: "E",
    5: "L"
}

chances = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,5]

class labubu:
    def __init__(self, name, efficiency, age, gender):
        self.name = name
        self.efficiency = efficiency
        self.age = age
    
    def kill(self):
        print(f'{self.name} has been killed!')
        del self

    def boost(self):
        self.efficiency += 20
        print(f'{self.name} efficiency increased to {self.efficiency}!')
        self.age -= 1

    def combine(self, second_labubu):
        self.efficiency = (self.efficiency + second_labubu.efficiency) * 1.5
        self.age = (self.age + second_labubu.age) / 2 
        print(f'{self.name} and {second_labubu.name} have combined!')
        del second_labubu
    
    def givehead(self, second_labubu):
        if self.gender == second_labubu.gender:
            print("They are not suitable for giving head to each other!")
            print("Unlock gender change tool to perform this act!")
        else:
            if self.gender == "M":
                self.efficiency += 50 
            else:
                second_labubu.efficiency += 50
            print(f'{self.name} and {second_labubu} have given head!')

    def sextransfer(self):
        self.gender = "M" if self.gender == "F" else self.gender = "F"     

def rolling():
    show = ['','','','','','','','','']
    for i in range(len(show)):
        a = random.randint(0,len(chances)-1)
        b = chances[a]
        if b in rarity:
            show[i] = rarity[b]
    print("Rolling for your labubu......")
    print('                ↓')
    for i in range(50):
        c_show = [f"\033[{colors[char]}m{char}\033[0m" if char in colors else char for char in show]
        print('   '.join(c_show), end='\r')
        time.sleep(i/70)
        show = show[-1:] + show[:-1]
        a = random.randint(0,len(chances)-1)
        b = chances[a]
        if b in rarity:
            show[0] = rarity[b]
    return show[4]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bold(text):
    return f"\033[1m{text}\033[0m"

def rules():
    clear()
    print('''
This is the rules of the Ho Man Tin Simulator game.
In this game, you will cosplay as Ho Man Tin, our beloved teacher.
Your goal in this game, is to farm labubus as much as possible.
The labubus can generate a currency called:
        '''
        )
    print(bold("load"))
    print('''
You will have tools to help you gain load, but you have to buy them!
Good luck!
        '''
        )

def exitgame():
    home()

def home():
    clear()
    print
