# Create a simple shopping cart program.

# The Welcome Message
print("==========================================================")
print("||           Welcome To Your Shopping Cart!             ||")
print("==========================================================")
print("||                                                      ||")
print("||                      _______                         ||")
print("||                     //  ||\\ \\                        ||")
print("||                ____//___||_\\ \\___                    ||")
print("||                \\      __      //                     ||")
print("||                 \\____(oo)____//                      ||")
print("||                      (_)(_)                          ||")
print("||                                                      ||")
print("==========================================================")

# Variables
foods = []
prices = []
total = 0

# The Main Program
while True:
    food = input("What food would you like to buy? (Press q to quit): \n")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"What is the price for {food}: \n$"))
        foods.append(food)
        prices.append(price)

print("==========================================================")
print("||                Your Shopping Cart!                   ||")
print("==========================================================")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your Total Is: ${total}")