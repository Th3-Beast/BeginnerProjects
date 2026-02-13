"""
- This is a basic program designed for Day 2 of the 100 Days Of Code course from Dr Angela Yu on Udemy.
- This  program Covers the basics of input() functions, Variables and some basic math operations.
- This program is a little more tricky than the Band Name Generator program.
  It involves the use of Type Conversions and the use of P.E.M.D.A.S
- P.E.M.D.A.S (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction)
"""

print("========================================")
print("Welcome to the Tips Split Calculator")
print("========================================\n")

# Collect the bill amount from the use - note that the bill may be an amount with a decimal value.
bill = float(input("What was the total bill? \n$"))

# Collect the tip amount from the user, Give the user a few numbers to chose from.
tip = int(input("What percentage tip would you like to give? 10, 12, 15 or 20\n"))

# Ask the user how many people are there that you would like to split the bill with.
people = int(input("How many people to split the bill?\n"))

# Once you have collected the input from the user begin the calculation.

# Calculate the tip amount and add it to the bill.
bill_with_tip = bill * (1 + tip / 100)

# Grab the total amount and divide the total by the number of people you are splitting the bill with.
per_person = bill_with_tip / people

print(f"Each person should pay: ${round(per_person, 2)}")