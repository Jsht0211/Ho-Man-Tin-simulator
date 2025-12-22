#this is the ho man tin sumulation code
import time 
import random
import math
import os 

tools_owned = {
    "booster":0,
    "horny_potion":0,
    "combine_potion":0,
    "sexchange_potion":0
}

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

Player = {
    "name":'',
    "money": 20,
    "level":0
}

class Labubu:
    def __init__(self, name, efficiency, age, gender):
        self.name = name
        self.efficiency = efficiency
        self.age = age
        self.gender = gender

    def __str__(self):
        return ("Name: " + self.name + '\n' +
                "Efficiency: " + str(self.efficiency) + '\n' +
                "Age: " + str(self.age) + '\n' +
                "Gender: " + self.gender)

    def __repr__(self):
        return "<Labubu Object>\n" + str(self)
    
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
    
    def giveHead(self, second_labubu):
        if self.gender == second_labubu.gender:
            print("They are not suitable for giving head to each other!")
            print("Unlock gender change tool to perform this act!")
            return 0
        else:
            if self.gender == "M":
                self.efficiency += 50 
            else:
                second_labubu.efficiency += 50
            print(f'{self.name} and {second_labubu} have given head!')
            return 1

    def sexTransfer(self):
        if self.gender == "F":
            self.gender = "M" 
        else: 
            self.gender = "F"     

def quickOpen():
    a = chances[random.randint(0,len(chances)-1)]
    if a in rarity:
        b = rarity[a]
    print("You have gotten a labubu with the",b,"rarity!")
    return b

def rolling():
    clear()
    show = ['','','','','','','','','']
    for i in range(len(show)):
        a = random.randint(0,len(chances)-1)
        b = chances[a]
        if b in rarity:
            show[i] = rarity[b]
    print("Rolling for your labubu......")
    print('                ↓')
    for i in range(40):
        c_show = [f"\033[{colors[char]}m{char}\033[0m" if char in colors else char for char in show]
        print('   '.join(c_show), end='\r')
        time.sleep(math.log(i+1)/10)
        show = show[-1:] + show[:-1]
        a = random.randint(0,len(chances)-1)
        b = chances[a]
        if b in rarity:
            show[0] = rarity[b]
    print()
    print("You have gotten a labubu with the",show[5],"rarity!")
    return show[5]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def flashingText(text,delay_in_sec,times_flashed):
    for i in range(times_flashed):
        print(text)
        time.sleep(delay_in_sec)
        clear()
        time.sleep(delay_in_sec)

def printStepByStep(text,delay_in_sec,stop_time_in_sec):
    for i in range(len(text)):
        print(text[i],end = '',flush = True)
        time.sleep(delay_in_sec)
    time.sleep(stop_time_in_sec)

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
By using load, you can buy weapons and aromor to increase your power.
There are multiple levels to this game and each level has its own boss.
Once you reach level 3, you beat the game!
Good luck!
        '''
        )
    print("Press anything to return to the homepage:")
    input()
    home()

def exitGame():
    print("Thank you for playing.")
    exit()

def home():
    clear()
    print(bold("This is the home page"))
    print('''
Welcome to Ho Man Tin simulator.
-----------------------------------------------------------------------------
Press 0 to quit the game
Press 1 to start the game
Press 2 to learn the rules
Press 3 to learn the plot
Press 4 to experience infinite gambling, infinite joy
-----------------------------------------------------------------------------         
        '''
        )
    user = input()
    while type(user) == str:
        try:
            user = int(user)
            while user > 4 or user < 0:
                user = input("Number out of range, input again:")
        except ValueError:
            user = input("Wrong data type, input again:")
    if user == 0:
        exitGame()
    elif user == 1:
        clear()
        printStepByStep(f"Hey {Player['name']}, just Jessie here checking you out.",0.05,1)
        clear()
        printStepByStep("You remember your plan to discover the truth of this pandemic?",0.05,1)
        clear()
        printStepByStep("Hey...",0.05,1)
        clear()
        printStepByStep("I've found these kind of creatures...",0.05,1)
        clear()
        printStepByStep("They produce like these kind of liquid...",0.05,1)
        clear()
        printStepByStep("You can eat it and i think we can make great money off it...",0.05,1)
        clear()
        printStepByStep("I have to go tho, bye!",0.05,1)
        clear()
        flashingText("Jessie ended the call",1,3)
        clear()
        printStepByStep("A month later, you find yourself in a lab with labubus",0.05,1)
        startMain()

    elif user == 2:
        rules()
    elif user == 3:
        plot()
    elif user == 4:
        while True:
            rolling()
            user = input("Press anything to continue(type quit to go back to homepage):")
            user = user.lower()
            if user == "quit":
                home()

def plot():
    clear()
    print('''
You are the one and only Ho Man Tin.
In the year 2050, the world as we know it has vanished due to the devastating pandemic.
Only around 10 thousands humans survive, living in settlements scattered around the globe.
Living on limited supplies of wheat, livestock is a thing of the past.
You, as the one of the lucky survivors of the war has discovered a special animal called:
        ''')
    print(bold("Labubu"))
    print('''
You discovered that they can produce a liquid called load.
You decided to make use of that and go on a journey of discovering the truth...
        '''
        )
    print("Press anything to return to the homepage:")
    input()
    home()

def buyToolsPage():
    clear()
    print(bold("Tools Market"),end = '')
    print('''
---------------------------------------------------------
Here you can buy tools to help you collect more loads.
Press the corresponding keys to buy the tools.
---------------------------------------------------------
        '''
        )

#main part
clear()
print(bold("Welcome to Ho Man Tin simulator"))
print('''
This is a game where you can fulfill your fantasy of being Ho Man Tin.
You can collect labubus, controll them, make them work.
Must importantly, use the load, buy weapons and conquer the world.
You won't get much load... Will you?
        '''
        )
print("Press anything to continue.")
input()
clear()
Player["name"] = input("What is your name?")
while Player["name"] == '':
    Player["name"] = input("Username cannot be empty. What is your name?")
print("Welcome,",Player["name"]+"!")
print("Press anything to continue.")
input()
while True:
    home()  


