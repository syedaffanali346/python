# Problem: Given a string, find the first non-repeated character

string = "teeterhdfasdhfjhd"
for char in string:
    if string.count(char) == 1:
        print(char)
        break