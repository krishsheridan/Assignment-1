import Role1 #import all the other modules
import Role2
import Game

def main():
    player_role = None #initialize role
    #############################################################################
    #Welcome Screen and role selection
    print("Welcome to the Text Adventure Speedrun")
    print("Choose your role: \n1. Nerd (Strength: -1, Dexterity: 1, Intelligence: 4, Health: 0)\n2. Beefman (Strength: 2, Dexterity: 0, Intelligence: -1, Health: 1)")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        player_role = Role1.initialize_role()
    else:
        player_role = Role2.initialize_role()

    Game.challenge1(player_role) #Run game challenges
    Game.challenge2(player_role)
    Game.challenge3(player_role)

    #############################################################################
    #Thank you for playing screen
    print("Thank you for playing Text Adventure Speedrun!") 

main()


