# Create a simple temperature converter that takes the current unit and converts it to the opposite unit.
# This project focuses on using user input, operators, conditional statements and fstring manipulation.

# The Welcome Message
print("==========================================================")
print("||            Welcome To The TEMP Converter!            ||")
print("==========================================================")
print("|| Things To Remember:                                  ||")
print("||                                                      ||")
print("|| * °F = (temp * 9) / 5 + 32                           ||")
print("||                                                      ||")
print("|| * °C = (temp - 32) * 5 / 9                           ||")
print("||                                                      ||")
print("==========================================================")

# Variables
unit = input("Is this temperature in °C or °F? (Type C or F)\n").upper()
temp = float(input("Enter the temperature: \n"))

# The Main Program
if unit == "C":
    result = round((temp * 9) / 5 + 32, 2)
    print(f"Your temperature is {result}°F")
elif unit == "F":
    result = round((temp - 32) * 5 / 9, 2)
    print(f"Your temperature is {result}°C")
else:
    print(f"{unit} is not a valid unit")