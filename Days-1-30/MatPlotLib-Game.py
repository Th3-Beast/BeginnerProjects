# Create a fun game that takes the users input and creates a fun little story out of the users input.
# This project focuses on using user input and fstring manipulation.

# The Welcome Message
print("==========================================================")
print("|| Welcome To The World Of MatPlotLib Story Telling     ||")
print("==========================================================")
print("|| Things To Remember:                                  ||")
print("||                                                      ||")
print("|| * An adjective is a description                      ||")
print("|| * A noun is a person, place, thing                   ||")
print("|| * A verb is an action, state, or occurrence          ||")
print("||                                                      ||")
print("==========================================================")

# The Variables
adjective1 = input("What is the first adjective you'd like you use? \n")
adjective2 = input("What is the second adjective you'd like you use? \n")
adjective3 = input("What is the third adjective you'd like you use? \n")
noun1 = input("What noun would you like you use? \n")
verb1 = input("What verb would you like you use? Use a ver ending in ('ing') \n")

# The main story
print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}")
