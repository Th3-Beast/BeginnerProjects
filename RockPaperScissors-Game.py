# Rock Paper Scissors - Basic CLI Version (No Functions)
# This game was designed to be a fun project for beginners working through the 100 Days Of Code from Dr Angela Yu 
# This project introduces the random function alongside the previous lessons of Logic

import random

# Welcome message and options
print(
    "***************** Welcome To My Rock-Paper-Scissors Game **********************"
    "\n*******************************************************************************"
    "\n*                                OPTIONS                                      *"
    "\n*******************************************************************************"
    "\n* [1] - Rock                                                                  *"
    "\n* [2] - Paper                                                                 *"
    "\n* [3] - Scissors                                                              *"                   
    "\n*******************************************************************************"
)

# ASCII Art for choices
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("\nLet's play one round! Type 'q' to quit.\n")

# Score tracking (will only show for one game)
player_wins = 0
computer_wins = 0
ties = 0

print("---------------------------------------------")
print(f"  Score  →  You: {player_wins}   Computer: {computer_wins}   Ties: {ties}")
print("---------------------------------------------\n")

# Show options
print(
    "*******************************************************************************"
    "\n*                                OPTIONS                                      *"
    "\n*******************************************************************************"
    "\n* [1] - Rock                                                                  *"
    "\n* [2] - Paper                                                                 *"
    "\n* [3] - Scissors                                                              *"
    "\n*******************************************************************************"
)

player_input = input("\nPlease select an option (1, 2 or 3): ").strip()

# Check if user wants to quit
if player_input.lower() == 'q':
    print("\nThanks for playing! Goodbye!")
else:
    # Check valid input
    if player_input not in ['1', '2', '3']:
        print("\nInvalid choice! Please enter 1, 2, or 3 next time.")
    else:
        # Player's choice
        if player_input == '1':
            player_choice = "Rock"
            player_art = rock
        elif player_input == '2':
            player_choice = "Paper"
            player_art = paper
        else:
            player_choice = "Scissors"
            player_art = scissors
        
        # Computer's random choice
        computer_options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(computer_options)
        
        # Computer's art
        if computer_choice == "Rock":
            computer_art = rock
        elif computer_choice == "Paper":
            computer_art = paper
        else:
            computer_art = scissors
        
        # Show the battle
        print("\n" + "=" * 50)
        print("                  YOU chose:")
        print(player_art)
        print("\n             COMPUTER chose:")
        print(computer_art)
        print("=" * 50)
        
        print(f"\nYou: {player_choice}          Computer: {computer_choice}\n")
        
        # Decide winner
        if player_choice == computer_choice:
            print("It's a TIE!")
            ties = ties + 1
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            print("YOU WIN! 🎉")
            player_wins = player_wins + 1
        else:
            print("Computer wins... 😔")
            computer_wins = computer_wins + 1
        
        # Show final score for this round
        print("\nFinal score this game:")
        print(f"You: {player_wins}   Computer: {computer_wins}   Ties: {ties}")
        
        print("\nGame over. Run the program again to play another round!")
        print("See you next time! ✊📄✂️")
