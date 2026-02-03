"""
- This is a basic program designed for Day 1 of the 100 Days Of Code course from Dr Angela Yu on Udemy.
- This  program Covers the basics of print() and input() functions and Variables.
"""

print("========================================")
print("Welcome to the Band Name Generator")
print("========================================\n")

# Ask the user which City they were born in, add the result to a variable
city = input("What is the name of the city you grew up in?\n")

# Ask the user for the name of their pet, add the result to a variable
pet = input("What is your pet's name?\n")

# Take both these results and add them together producing a band name
# that combines the name of the city and the name of their pet.
print("Your Band Name could be " + city + " " + pet)