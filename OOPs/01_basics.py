import math
# class Students:
#     name = "Affan"

# std1 = Students()
# print(std1.name)

# std2 = Students()
# print(std2.name)


# class Students:
#     def __init__(self):
#         print("Adding new object in database...!")
#     name = "Affan"

# std1 = Students()
# print(std1.name)


# class Students:
#     college_name = "ABC College" # Class attribute

#     def __init__(self, name, marks):
#         self.name = name # Object attribute
#         self.marks = marks
#         print("Adding new object in database...!")

#     def welcome(self):
#         print("Welcome studnet", self.name)

# std1 = Students("Ammar", 97)
# print(std1.name, std1.marks)

# print("...")

# std2 = Students("Zaid", 88)
# print(std2.name, std2.marks, std2.college_name)
# std2.welcome()


# Practice Question
# class Student:
#     def __init__(self, name, english, math, physics):
#         self.name = name
#         self.english = english
#         self.math = math
#         self.physics= physics

#     def average_marks(self):
#         sum = self.english + self.math + self.physics
#         average = sum / 3
#         print("Hi", self.name, "your average score is", math.floor(average))

        
# std1 = Student("Affan",97, 88, 68)
# std1.average_marks()


class Students:
    def __init__(self, name):
        self.name = name

std1 = Students("Shradha")
print(std1.name)
del std1.name # Delete The Attribute
print(std1.name)