#Problem: Movie tickets are priced based on age: 12$ for adults(18 and over), $8 for children, Everyone gets a $2 discount on Wednesday

age = 65
day = "Wednesday"

# if day == "Wednesday":
#     if age >= 18:
#         print(f"Actual ticket price ${12} with discount of wednesday ${12 - 2}.")
#     else:
#         print(f"Actual ticket price ${8} with discount of wednesday ${8 - 2}.")
# else:
#     if age >= 18:
#         print(f"Ticket price ${12}.")
#     else:
#         print(f"Ticket price ${8}.")

#New Technique
price = 12 if age>=18 else 8
if day == "Wednesday":
    price -= 2

print(price)