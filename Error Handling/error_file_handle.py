# Manually Method
file = open("test1.txt", "w") # mode = "w" => agar file nahi hogi tw khud banjati is mode waja se warna error aata he
try:
    file.write("Testing 1")
finally:
    file.close()


# Advance Method
with open("test2.txt", "w") as file: # with wale tareeqe se close() ki zaroorat nahi parti
    file.write("Testing 2")

with open("test2.txt", "r") as file:
    print(str(file.readline()))