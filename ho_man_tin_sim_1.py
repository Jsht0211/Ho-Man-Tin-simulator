#view source code only in risk of spoiler
import time 
import random
import math
import os 

tools_owned = {
    "booster":0,
    "horny_potion":0,
    "combine_potion":0,
    "sexchange_potion":0,
    "totem_of_undying":0
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

class Bosses:
    def __init__(self, name : str, level_correspond : int, hp : int, defence_stat : int, attack_stat : str, attack_type : str, description : str):
        self.name = name
        self.level_correspond = level_correspond
        self.hp = hp
        self.defence_stat = defence_stat
        self.attack_stat = attack_stat
        self.attack_type = attack_type
        self.description = description
    
    def __str__(self):
        return ("Name:" + self.name + '\n' + 
                "Level:" + str(self.level_correspond) + '\n' +
                "HP:" + str(self.hp) + '\n' + 
                "Defence stat:" + str(self.defence_stat) + '\n' +
                "Attack stat:" + str(self.attack_stat) + '\n' + 
                "Type of attack:" + self.attack_type + '\n')

    def __des__(self):
        return (self.description)

class Items:
    def __init__(self, name : str, type_of_item : str, __level_required_to_obtain : int, __base_price : int, price : float):
        self.name = name
        self.level_required_to_obtain = __level_required_to_obtain
        self.base_price = __base_price
        self.type_of_item = type_of_item
        self.price = price

    def checkAbleToObtain(self,Player : object):
        if Player.level >= self.level_required_to_obtain:
            return True
        return False

    def __str__(self):
        return ("Name:" + self.name + '\n' + 
                "Type:" + self.type_of_item + '\n' +
                "Price:" + str(self.price) + '\n') 
    
    def __repr__(self):
        return "<Items Object>\n" + str(self)

    
class Armor(Items):
    def __init__(self, name : str, type_of_item : str, __level_required_to_obtain : int, __base_price : int, price : float, defence_stat : int, added_hp : int):
        super().__init__(name, type_of_item, __level_required_to_obtain, __base_price, price)
        self.defence_stat = defence_stat
        self.added_hp = added_hp

    def __str__(self):
        return (super().__str__() + 
                "Defence stat:" + str(self.defence_stat) + '\n' + 
                "Added hp:" + str(self.added_hp))

class Tools(Items):
    def __init__(self, name : str, type_of_item : str, __level_required_to_obtain : int, __base_price : int, price : float, effect : str):
        super().__init__(name, type_of_item, __level_required_to_obtain, __base_price, price)
        self.effect = effect
    
    def __str__(self):
        return (super().__str__() + 
                "Effect:" + str(self.effecct))

class Weapons(Items):
    def __init__(self, name : str, type_of_item : str, __level_required_to_obtain : int, __base_price : int, price : float, attack_stat : int):
        super().__init__(name, type_of_item, __level_required_to_obtain, __base_price, price)
        self.attack_stat = attack_stat

    def __str__(self):
        return (super().__str__() +
                "Attack stat:" + str(self.attack_stat))

class Player:
    def __init__(self, name, money, level, Labubu_slot, Labubu_owned, helmet_equiped, chestplate_equiped, pants_equiped, shoes_equiped, sword_equiped,
                long_range_equiped, attack_stat, defence_stat, load_efficiency_in_sec, lives, hp):
        self.name = name
        self.money = money
        self.level = level 
        self.Labubu_slot = Labubu_slot
        self.Labubu_owned = Labubu_owned
        self.helmet_equiped = helmet_equiped
        self.chestplate_equiped = chestplate_equiped
        self.pants_equiped = pants_equiped
        self.shoes_equiped = shoes_equiped
        self.sword_equiped = sword_equiped
        self.long_range_equiped = long_range_equiped
        self.attack_stat = attack_stat
        self.defence_stat = defence_stat
        self.load_efficiency_in_sec = load_efficiency_in_sec
        self.lives = lives
        self.hp = hp
    
    def takeDamage(self, damage_taken : int):
        self.hp -= damage_taken

    def advanceLevel(self):
        self.level += 1
        self.Labubu_slot += 10

    def __str__(self):
        return ("Name:" + self.name + '\n' +
                "Money:" + self.money + '\n' +
                "Level:" + self.level + '\n' +
                "Labubu slots:" + self.Labubu_slot + '\n' +
                "Labubu owned:" + self.Labubu_owned + '\n' + 
                "Helmet equiped:" + self.helmet_equiped + '\n' +
                "Chestplate equiped:" + self.chestplate_equiped + '\n' +
                "Pants equiped:" + self.pants_equiped + '\n' +
                "Shoes equiped:" + self.shoes_equiped + '\n' +
                "Sword equiped:" + self.sword_equiped + '\n' +  
                "Long range equiped:" + self.long_range_equiped + '\n' +
                "Attack stat:" + self.attack_stat + '\n' +
                "Defence stat:" + self.defence_stat + '\n' +
                "Load efficiency in sec:" + self.load_efficiency_in_sec + '\n' +
                "Lives:" + self.lives)

    def __repr__(self):
        return "<Player Object>\n" + str(self)

Player = Player("",20,0,10,0,"","","","","","",0,0,0,1,100)

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

    def giveHead(self, second_labubu):
        if self.gender == second_labubu.gender:
            print("They are not suitable for giving head to each other!")
            print("Unlock gender change tool to perform this act!")
            return 0
        else:
            if self.gender == "M":
                self.efficiency += 50 
                print(f"{second_labubu.name} has given {self.name} head!") 
            else:
                second_labubu.efficiency += 50
                print(f"{self.name} has given {second_labubu.name} head!")      
            return True

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

def flashingText(text : str,delay_in_sec : float,times_flashed : int):
    for i in range(times_flashed):
        print(text)
        time.sleep(delay_in_sec)
        clear()
        time.sleep(delay_in_sec)

def printStepByStep(text : str,delay_in_sec : float,stop_time_in_sec : float):
    for i in range(len(text)):
        print(text[i],end = '',flush = True)
        time.sleep(delay_in_sec)
    time.sleep(stop_time_in_sec)

def bold(text : str):
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
Once you reach level 5, you beat the game!
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
    global start_time
    global temp_time
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
        printStepByStep(f"Hey {Player.name}, just Jessie here checking you out.",0.05,1)
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
        start_time = time.time()
        temp_time = time.time()
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

def startMain():
    global temp_time
    clear()
    now_time = time.time()
    Player.money = Player.money + (now_time - temp_time) * Player.load_efficiency_in_sec 
    temp_time = time.time()
    time_played = now_time - start_time
    print(bold("The HMT lab"))
    print(f'''
You are in level: {Player.level}
Time played in seconds: {f"{time_played:.2f}"}
Your money you have now: ${Player.money}
-------------------------------------------------------------
This is the menu of the game.
-------------------------------------------------------------
Press 0 to quit the game
Press 1 to roll a labubu
Press 2 to manage your labubus
Press 3 to manage your inventory
Press 4 to buy tools
Press 5 to buy armor 
Press 6 to buy weapons
Press 7 to view your journey
Press enter to refresh
        '''
        )
    user = input()
    while type(user) == str:
        try:
            user = int(user)
            if user > 7 or user < 0:
                user = input("Input invalid, input again:")
        except ValueError:
            if user == '':
                startMain()
            else:
                user = input("Input invalid, input again:")
    if user == 0:
        exitGame()
    elif user == 1:
        buyLabubuCrate()        #check money is enough, quick open, rolling and initiate that labubu shit, prob description?idk i will do this later
    elif user == 2:
        manageLabubu()      #view slots left,show some attributes, can select one labubufor detail stats
    elif user == 3:
        playerInventory()       #do grouping maybe???
    elif user == 4:
        buyToolsPage()      
    elif user == 5:
        buyArmorPage()
    elif user == 6:
        buyWeaponPage()
    elif user == 7:
        journeyMap(Player)        #include boss stats, not done yet, need to include boss stats 

def journeyMap(Player : object):
    level = Player.level
    print("Your current level:", level)
    Map = [
            ["s               ","1","               ","2","               ","3","               ","4","               ","5"],
            ["^---------------","x","---------------","x","---------------","x","---------------","x","---------------","x"]
    ]
    for i in range(1,level*2,2):
        Map[1][i] = "^"
    for row in Map:
        print("".join(row))
    user = input("Input the number of the level you want to view(input nothing to go back to main page):")                      
    while type(user) == str:
        try:
            level_viewing = int(user)
            if level_viewing > 5 or level_viewing < 1:
                user = input("Input the number of the level you want to view(out of range):")
        except ValueError:
            if user == "":
                startMain()
            else:
                user = input("Input invalid, input again:")

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
    print("Press anything to go back:")
    input()
    startMain()

#main part
clear()
print(bold("Welcome to Ho Man Tin simulator"))
print('''
This is an RPG game where you can fulfill your fantasy of being Ho Man Tin, as one of the survivors of the global pandemic.
You discovered labubus which make loads which makes you money.
You decided to buy armor, tools, weapons to go on a journey to discover the truth of the pandemic.
You won't get lost... Will you?
        '''
        )
print("Press anything to continue:")
input()
clear()
Player.name = input("What is your name?")
while Player.name == "":
    Player.name = input("Username cannot be empty. What is your name?")
print("Welcome,",Player.name+"!")
print("Press anything to continue:")
clear()
user = input(f"{Player.name}, do you love Ho Man Tin?(hint: say yes)")
user = user.lower()
permit = True
if user != "yes":
    permit = False
assert permit == True , "Go kill yourself..."       #no need to use assert but i just learned it so i wanna use
print("Great! Press anything to continue:")
input()
while True:
    home()  
