"""
Treasure Island - A Simple Text Adventure Game
Perfect for Python beginners!
"""

print(r'''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

# First choice
print("You're In the middle of a forrest and have sumbled onto a crossroad. Where would you want to go?")
choice1 = input('Type "left" or "right": ').lower()

if choice1 == "left":
    # Second choice
    print("\nYou come to a lake. There is an island cave in the middle of the lake.")
    choice2 = input('Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    
    if choice2 == "wait":
        # Third choice
        print("\nYou arrive at the cave's entrance. There is an opening in the distance with 3 doors.")
        print("One red, one yellow and one blue.")
        choice3 = input("Which color do you choose? ").lower()
        
        if choice3 == "red":
            print("\nBurned by fire. Game Over.")
        elif choice3 == "yellow":
            print("\nYou found the treasure! You Win!")
            print('''
              ___________
             /\\ ________ \\
            /  \\ \\______\\ \\
           / /\\ \\ \\  / /\\ \\
          / / /\\ \\ \\/ / /\\ \\
         / / /__\\ \\ \\/_/__\\/
        / /_/___/\\ \\ \\ \\
        \\ \\ \\   \\ \\/\\ \\ \\
         \\ \\ \\___\\/ /\\ \\ \\
          \\ \\/_____/  \\ \\_\\
           \\/_________/\\/_/
         
          💎 TREASURE! 💎
            ''')
        elif choice3 == "blue":
            print("\nEaten by beasts. Game Over.")
        else:
            print("\nGame Over.")
    else:
        print("\nAttacked by trout. Game Over.")
else:
    print("\nAttacked by a goblin. Game Over.")
