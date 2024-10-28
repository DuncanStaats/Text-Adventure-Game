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
print("Groggly, you think of what to do or else you fear you will die.\n1. Will you scream for help and pray some one will hear you.\n2. Will you stay quiet and try to unchain yourself.")
print("Be warned, if you answer the question without the proper answer you will not see the end.")
choice_1 = int(input("1 or 2: "))

if choice_1 == 1:
    print("He"+"e"*6+"l"*7+"p")
    print("A man, from the shadows, takes a hand that taste of grim and salt to your mouth.")
    print("S"+"hhh"+"u"*11+".","You'll wake the guards, are you trying to be whipped boy.")

elif choice_1 == 2:
    print("You move your chained hand to your mouth to produce a needle.")
    print("You rattle with your chains using the needle and with a Clink! Your hands are set free")
    print("Before you finish a man sweeps out of the shaddows and tackles you to get your needle. You loose your grip and the man takes it with him back into the shadows of the room.")
else:
    print("You have decided to answer poorly, you get stabbed by another while chained and bleed to death.")
    print("You have died and will not be returned, please restart and be even more cautious of your future answers.")