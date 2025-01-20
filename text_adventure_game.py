import random

def intro_screen():
    intro_art = r'''
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
    print()

def player_status(player_score: dict) -> None:
    print(f"Your current score is {player_score['score']}")

def choice_1(player_score):
    print(f"Do you\n1)Scream for help"
          f"\n2)Stay quiet and try to free yourself"
          f"\n3)Call the guard")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            Inmate_friend(player_score) 
            return player_choice
        elif player_choice == 2:
            Inmate_attack()
            return player_choice
        elif player_choice == 3:
            Guard_friend(player_score)
            return player_choice
        else:
            print("Invalid choice")
            continue

def Inmate_friend(player_score):
    player_score['score'] += 10
    print("HHHHEEEELLLL⎯")
    print("You meet an inmate and he tells you to stop or you will wake up the guards." 
          f"\nHe helps you unlock yourself and decides to show you his map to a treasure."
          f"\nYou and the inmate come up with a plan to escape to the rowboats and collect the treasure."
          f"\nHow do you plan to escape?")
    player_status(player_score)
    print()

def Inmate_attack():
    print("You try and free yourself but end up getting attacked by an inmate."
          f"\nYou wrestle the inmate and stand up to attack him when you slip and crack your head open.")
    print()

def Guard_friend(player_score):
    player_score['score'] += 10
    print("An inmate tells you to shut up but, you ignore him and continue yelling."
          f"\nThe guard asks you what you want. You ask the guard to speak to the Captain."
          f"\nThe Captain comes and you⎯")
    player_status(player_score)
    print()

def choice_2a(player_score):
    print(f"Do you\n1)Distract the guards"
          f"\n2)Sneak out at night"
          f"\n3)Leave now and make a break for it")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            distract_guard(player_score)
            return player_choice
        elif player_choice == 2:
            sneak_out()
            return player_choice
        elif player_choice == 3:
            leave_now(player_score)
            return player_choice
        else:
            print("Invalid choice")
            continue

def distract_guard(player_score):
    player_score['score'] += 5
    print("You are able to distract the guards successfully and make it on deck."
          f"\nYou run over and the inmate asks if we should gather supplies.")
    player_status(player_score)
    print()

def sneak_out():
    print("You and the inmate try and sneak out at night."
          f"\nYou run into a guard who thinks you are an intruder and he kills you.")
    print()

def leave_now(player_score):
    player_score['score'] += 10
    print("You and the inmate rush out and successfully evade the guards."
          f"\nYou rush over to the rowboats and set sail."
          f"\nYou get to the island and pull out the map while searching around."
          f"\nYou come across a treasure chest with a snake wrapped around it.")
    player_status(player_score)
    print()

def choice_2b(player_score):
    print(f"Do you\n1)Tell the Captain you are willing to work for him"
          f"\n2)Yell at the Captain for being unfair and demand he releases you")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            captain_worker(player_score)
            return player_choice
        elif player_choice == 2:
            yell_at_captain()
            return player_choice
        else:
            print("Invalid choice")
            continue

def captain_worker(player_score):
    player_score['score'] += 5
    print("The Captain agrees but, he tells you that you got to earn the right to be part of his crew."
          f"\nYou are going to have to fight his first mate."
          f"\nYou are prepping your attack.")
    player_status(player_score)
    print()

def yell_at_captain():
    print("The Captain looks at you, then looks at the guard and back to you."
          f"\nHe takes out his flintlock and shoots you.")
    print()

def choice_3aa(player_score):
    print(f"Do you\n1)Yes, you gather supplies"
          f"\n2)No, you don't gather supplies")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            yes_supplies(player_score)
            return player_choice
        elif player_choice == 2:
            no_supplies(player_score)
            return player_choice
        else:
            print("Invalid choice")
            continue

def yes_supplies(player_score):
    player_score['score'] += 10
    print("You and the inmate gather a canteen of water and some jerky."
          f"\nYou set sail and arrive at the island and begin to look around for the treasure."
          f"\nYou find the treasure chest.")
    player_status(player_score)
    print()

def no_supplies(player_score):
    player_score['score'] += 5
    print("You don't gather any supplies and set sail immediately."
          f"\nYou arrive at the island and search for the treasure."
          f"\nYou find the treasure chest.")
    player_status(player_score)
    print()

def choice_3ab(player_score):
    print(f"Do you\n1)Fight the snake and start digging"
          f"\n2)Run away and wait to come back")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            fight_snake(player_score)
            return player_choice
        elif player_choice == 2:
            hide_from_snake(player_score)
            return player_choice
        else:
            print("Invalid choice")
            continue

def fight_snake(player_score):
    player_score['score'] += 5
    chance_1 = random.randint(0, 4)
    if chance_1 in [0, 3]:
        print("You fight the snake off and begin to open the treasure chest.")
    else:
        print("You got bit by the snake and died.")
    player_status(player_score)
    print()

def hide_from_snake(player_score):
    print("You run away and wait for the snake to leave."
          f"\nThe snake has left and you begin to open the treasure chest.")
    player_status(player_score)
    print()

def choice_3b(player_score):
    print(f"Do you\n1)Take a swing with your fist"
          f"\n2)Try and kick him"
          f"\n3)Charge him and tackle him")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            fist_attack(player_score)
            return player_choice
        elif player_choice == 2:
            kick_attack(player_score)
            return player_choice
        elif player_choice == 3:
            charge_attack(player_score)
            return player_choice
        else:
            print("Invalid choice")
            continue

def fist_attack(player_score):
    chance_2a = random.randint(0, 9)
    if chance_2a in [0, 5]:
        print("You land the attack successfully and join the crew.")
        player_score['score'] += 10
        print("You and the crew arrive on an island and the Captain orders everyone to begin looking for treasure."
          f"\nYou go looking around and trip on a mound in the sand."
          f"\nYou start digging and find a treasure chest.")
    else:
        print("You missed and got beat to death.")
        print("You and the crew arrive on an island and the Captain orders everyone to begin looking for treasure."
          f"\nYou go looking around and trip on a mound in the sand."
          f"\nYou start digging and find a treasure chest with nothing inside.")
    player_status(player_score)
    print()
def kick_attack(player_score):
    chance_2b = random.randint(0, 9)
    if chance_2b in [0, 4]:
        print("You land the attack successfully and join the crew.")
        player_score['score'] += 10
        print("You and the crew arrive on an island and the Captain orders everyone to begin looking for treasure."
          f"\nYou go looking around and trip on a mound in the sand."
          f"\nYou start digging and find a treasure chest.")
    else:
        print("You missed and got beat to death.")
        print("You and the crew arrive on an island and the Captain orders everyone to begin looking for treasure."
          f"\nYou go looking around and trip on a mound in the sand."
          f"\nYou start digging and find a treasure chest with nothing inside.")
    player_status(player_score)
    print()

def charge_attack(player_score):
    chance_2c = random.randint(0, 9)
    if chance_2c in [0, 2]:
        print("You land the attack successfully and join the crew.")
        player_score['score'] += 5
        print("You and the crew arrive on an island and the Captain orders everyone to begin looking for treasure."
          f"\nYou go looking around and trip on a mound in the sand."
          f"\nYou start digging and find a treasure chest.")
    else:
        print("You missed and got beat to death.")
        print("You and the crew arrive on an island and the Captain orders everyone to begin looking for treasure."
          f"\nYou go looking around and trip on a mound in the sand."
          f"\nYou start digging and find a treasure chest with nothing inside.")
    player_status(player_score)
    print()

def treasure_score(player_score):
    if player_score['score'] >= 25:
        print("You open the chest and find that it is filled with gold and jewels."
              f"\nYou have made it to the end and won the game, CONGRATULATIONS!")
    else:
        print("You have either been defeated or failed to achieve the required points to secure victory."
              f"\nGAME OVER!")

def main():
    player_score = {'score': 0}
    intro_screen()
    first_choice = choice_1(player_score)
    if first_choice == 1:
        second_choice = choice_2a(player_score)
        if second_choice == 1:
            choice_3aa(player_score)
        elif second_choice == 3:
            choice_3ab(player_score)
    elif first_choice == 3:
        second_choice = choice_2b(player_score)
        if second_choice == 1:
            choice_3b(player_score)
    treasure_score(player_score)

if __name__ == '__main__':
    main()