# Create a simple weight converter that takes the weight input from the user
# and converts it from lbs to kg or kg to lbs.
# This project focuses on using user input, operators, conditional statements and fstring manipulation.

# The Welcome Message
print("==========================================================")
print("|| Welcome To The Weight Converter!                     ||")
print("==========================================================")
print("|| Things To Remember:                                  ||")
print("||                                                      ||")
print("|| * LBS TO KG = lbs / 2.205                            ||")
print("||                                                      ||")
print("|| * KG TO LBS = kg X 2.205                             ||")
print("||                                                      ||")
print("==========================================================")

# Variables
units = 2.205

user_input = float(input("What is the weight? (Enter the number only) \n"))
unit_measurement = input("Would you like to convert to lbs or kg? (Enter lbs or kg) \n").lower()

# The Main Program
if unit_measurement == "kg":
    result = user_input / units # This means the number you used is in lbs
    print(f"Your Weight In KG is: {result}kg")
elif unit_measurement == "lbs":
    result = user_input * units # This means the number you used is in kgs
    print(f"Your Weight In lbs is: {result}lbs")
else:
    print("You have not entered a correct input. Please enter a correct input.")