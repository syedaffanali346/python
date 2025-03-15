books = {
    "name": "First Book",
    "author": "John Doe",
    "year": 2020
}

# books["pages"] = 100  # Add
# books.pop("author")  # Remove
# books.popitem()  # Remove last item
del books["author"]  # Remove
# print(books)

# books["name"] = "Second Book" # Update

# Printing
# print(books["name"])  # square bracket notation
# print(books.get("author"))  # get method

# print(books.get("dsfkdls")) # None
# print(books["adfklj"]) # KeyError

# iterate over keys
# for key in books.keys():
#     print(key)

# # iterate over values
# for value in books.values():
#     print(value)

# # iterate over items
# for key, value in books.items():
#     print(f"{key}: {value}")

# if "name" in books:
#     print("Yes")

# print(len(books))  # 3

squared_num = {x: x**2 for x in range(6)}
print(squared_num)