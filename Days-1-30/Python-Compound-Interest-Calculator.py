# Create a simple Compound Interest Calculator.
# This project focuses on using user input, operators, conditional statements, while loops and fstring manipulation.

# The Welcome Message
print("==========================================================")
print("||     Welcome To The Compound Interest Calculator!     ||")
print("==========================================================")
print("|| Things To Remember:                                  ||")
print("|| A = Final Amount                                     ||")
print("|| P = Initial Principal Balance                        ||")
print("|| r = Interest Rates                                   ||")
print("|| t = Number of Time Periods Elapsed                   ||")
print("||                                                      ||")
print("==========================================================")

# Variables
principle = 0
rate = 0
time = 0

total = principle * pow((1 + rate / 100), time)

# The Main Program
while True:
    principle = float(input("Enter The Principal Amount: "))
    if principle < 0:
        print("Principal Amount can't be less than zero.")
    else:
        break

while True:
    rate = float(input("Enter Your Interest Rate: "))
    if rate < 0:
        print("Interest Rate can't be less than zero.")
    else:
        break

while True:
    time = int(input("Enter The Time In Years: "))
    if time < 0:
        print("Time can't be less than zero.")
    else:
        break

print(f"Balance after {time} Year/s: ${total:.2f}")