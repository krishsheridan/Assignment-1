import random

#############################################################################
#Define Challenges, Roll dice, Calculate win or loss
def challenge1(role):
    print("Welcome to crossing the road in India.\nAttribute needed: Dexterity")
    roll = roll_two_dice()
    print("Dice roll: " + str(roll) + "\nDexterity: " + str(role["dexterity"]))
    print("Your total roll is your dice roll + your dexterity")
    if roll >= 5:
        print("You just won")
    else:
        print("You lose.")

def challenge2(role):
    print("Welcome to solving the impossible puzzle.\nAttribute needed: Intelligence")
    roll = roll_two_dice()
    print("Dice roll: " + str(roll) + "\nIntelligence: " + str(role["intelligence"]))
    print("Your total roll is your dice roll + your intelligence")
    if roll >= 6:
        print("You just won")
    else:
        print("You lose.")

def challenge3(role):
    print("Welcome to fighting Mike Tyson.\nAttribute needed: Strength")
    roll = roll_two_dice()
    print("Dice roll: " + str(roll) + "\nStrength: " + str(role["strength"]))
    print("Your total roll is your dice roll + your strength")
    if roll >= 7:
        print("You just won")
    else:
        print("You lose.")

#############################################################################
#Code to roll two dice
def roll_two_dice():
    input("Press Enter to roll dice")
    die = random.randint(1, 12)
    return die


