# Welcome user
print("Welcome to GC Fruit Market!")

# Step 1: Ask the user for their name and store it
user_name = input("What is your name? ")

# Step 2: Display a list of fruit: Apple, $2...Grape, $1...Orange, $3
apple = "Apple"
apple_price = 2
apples_to_buy = 0

grape = "Grape"
grape_price = 1
grapes_to_buy = 0

orange = "Orange"
orange_price = 3
oranges_to_buy = 0

#   - print fruit list numbering each fruit and their value
print(f"[1. {apple} ${apple_price}")
print(f"[2. {grape} ${grape_price}")
print(f"[3. {orange} ${orange_price}")


# Step 3: Allow the user to select and buy one of the fruits from the list
#      - prompt the user with input (" Welcome (customer_name). Which Fruit would you like to buy?")
#      - Track how many of each fruit has been bought
#      - print purchase detail such as "You bought 1 apple at $2" after selection is made
initial_question = int(input(f"Welcome {user_name}. Which fruit would you like to buy? "))

if initial_question == 1:
    apples_to_buy += 1
    print("You bought 1 apple at $2.")
elif initial_question == 2:
    grapes_to_buy += 1
    print("You bought 1 grape at $1.")
elif initial_question == 3:
    oranges_to_buy += 1
    print("You bought 1 orange at $3.")
else:
    print("sorry this is an invalid response.")
    # Step 4:  Give the user the option to buy another fruit or be done repeatedly until they do not want any more fruit
    #  - ask (Would you like to buy another piece of fruit? y/n)
    # while loop
follow_up_question = input("Would you like to buy another piece of fruit? y/n ")
while follow_up_question == "y":
    print(f"[1. {apple} ${apple_price}")
    print(f"[2. {grape} ${grape_price}")
    print(f"[3. {orange} ${orange_price}")
    question = int(input("Which fruit would you like to buy? "))
    if question == 1:
        print("You bought 1 apple at $2.")
        apples_to_buy += 1
    if question == 2:
        print("You bought 1 grape at $1.")
        grapes_to_buy += 1
    if question == 3:
        print("You bought 1 orange at $3.")
        oranges_to_buy += 1
    follow_up_question = input("Would you like to buy another piece of fruit? y/n ")
    continue
#   - if no display a string saying "Receipt for {name}" putting their name into the string
if follow_up_question == "n":
    print(f"Receipt for {user_name}")

# Step 5: Print the number of each fruit purchased
print(str(apples_to_buy) + "(s) at $" + str(apple_price) + ".00 a piece.")
print(f"{grapes_to_buy}(s) at ${grape_price}.00 a piece.")
print(f"{oranges_to_buy}(s) at ${orange_price}.00 a piece.")

# Step 6: Find and print the subtotal (amount of each fruit bought * its cost all added together)
subtotal_for_apples = apples_to_buy * apple_price
subtotal_for_grapes = grapes_to_buy * grape_price
subtotal_for_oranges = oranges_to_buy * orange_price
subtotal = subtotal_for_apples + subtotal_for_oranges + subtotal_for_grapes
print(f"Subtotal: {subtotal}")

# Step 7: Find and print the tax (5%)
tax = subtotal * 0.05
print(f"5% Tax: {tax}")

# Step 8: add the subtotal and tax to get the receipt total.
# - Print that
total = subtotal + tax
print(f"Total:{total} ")