# Inheritance

# # Single Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car started...!")

#     @staticmethod
#     def stop():
#         print("Car stoped...!")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# print(car1.name)
# car1.start()


# Multi-Level Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car started...!")

#     @staticmethod
#     def stop():
#         print("Car stoped...!")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Diesel")
# print(car1.type)
# car1.start()


# Multiple Inheritance
# class A:
#     varA = "class a"

# class B:
#     varB = "class b"

# class C(A,B):
#     varC = "class c"

# cla1 = C()
# print(cla1.varA)
# print(cla1.varB)
# print(cla1.varC)


class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started...!")

    @staticmethod
    def stop():
        print("Car stoped...!")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

car1 = ToyotaCar("Fortuner", "Electric")
print(car1.name)
print(car1.type)
car1.start()