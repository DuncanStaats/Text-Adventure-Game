def intro():
    intro_art =r'''
_______________________________________________________________________________
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_'''

    print(intro_art)
    print("You gaze upon what will be your last job.\nYou stare with such intensity that you don't even notice...")
    print("Thud!")
    print("Thump, Thump, Thump.\nYou wake up! You have a major headache and find out you are in chains.")
    print("Groggly, you think of what to do as you are stuck on a ship.\n1. Will you scream for help and pray some one will hear you.\n2. Will you stay quiet and try to unchain yourself.")

def choice1():
    while True:   
        choice_1 = int(input("1 or 2: "))

        if choice_1 == 1:
            print("He"+"e"*6+"l"*7+"p")
            print("A man, from the shadows, takes a hand that taste of grim and salt to your mouth.")
            print("S"+"hhh"+"u"*11+".","You'll wake the guards, are you trying to be whipped boy.")
            break

        elif choice_1 == 2:
            print("You move your chained hand to your mouth to produce a pick.")
            print("You rattle with your chains using the pick and with a Clink! Your hands are set free")
            print("Before you finish a man sweeps out of the shaddows and tackles you to get your pick.\nYou loose your grip and the man takes the needle with him back into the shadows of the room.")
            break

        else:
            print("You have decided to answer poorly, you get stabbed by another while chained and bleed to death.")
            print("You have died and will now be returned to you first choice. Please answer correctly next time.")
            continue

def choice2():
    while True:
        choice_2 = int(input("1, 2, or 3: "))
        
        if choice_2 == 1:
            print("You and your friend slowly make your way to the captains door.\nYou try and open the door and relize it is locked and move your way up to the helm. ")
            print("You step on a creaky floor board and wake the captain.\nThe captain yells and wakes everyone up and you and your friend die to the captain and the crew.")
            sub_choice2(1)
            break    

        elif choice_2 == 2:
            print("You creep your way to the crew quaters and have your friend watch the door.")
            print("You look around and fine nothing within the crew quaters and decide to leave before getting caught.")
            sub_choice2(2)
            break

        elif choice_2 == 3:
            print("You find a ton of supplies in the armory and cafeteria and now you have to choose what to bring:")
            print("1. Will you grab stale bread and a small knife, and a small canteen of water.\n2. Will you grab some jerky and bread along with a blunderbuss pistol and a cutlass and a medium size canteen of water")
            sub_choice2(3)
            break  

        else:
            print("You have decided to answer poorly, you get shot by the captian and bleed to death.")
            print("You have died and will now be returned to you last choice. Please answer correctly next time.")
            continue    

def sub_choice2(choice):
    while True:
        
        if choice == 1:
            print("You have died and will now be returned to the start.")
            break   

        elif choice == 2:
            print("You sneak on to the rowboat peacefully without alerting the guards.")
            break    

        elif choice == 3:
            sub_choice_1 = int(input("1 or 2: "))
            if sub_choice_1 == 1:
                print("You sneak on to the rowboat peacefully without alerting the guards.")
                break

            elif sub_choice_1 == 2:
                print("You drop the pistol and it fires waking up the crew and captain.")
                print("You and your friend die in this process and do not make it out alive.")
                break

intro()
choice1()
choice2()