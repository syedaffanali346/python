# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = 5
for i in range(1, 11):
    if i == 5:
        continue
    print(f"{number} * {i} = {i * number}")