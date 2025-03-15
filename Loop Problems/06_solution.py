# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("enter a number b/w 1 and 10: "))
    if number >= 1 and number <= 10:
        print("Thanks!")
        break
    else:
        print("Invalid number please try again")