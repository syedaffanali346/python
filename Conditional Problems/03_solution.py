#Problem: Assign a letter grade based on student's score: A(90 - 100), B(80 - 89), C(70 - 79), D(60 - 69), 
# F(below 60)

score = 100

# if score >100:
#     print("You entered a wrong number!")
# else:
#     if score>=90:
#         print("Grade A")
#     elif score>=80:
#         print("Grade B")
#     elif score>=70:
#         print("Grade C")
#     elif score>=60:
#         print("Grade D")
#     else:
#         print("F")

# New Method
if score >= 101:
    print("please verify your grade again!")
    exit()

if score>=90:
    grade = "A"
elif score>=80:
    grade = "B"
elif score>=70:
    grade = "C"
elif score>=60:
    grade = "D"
else:
    grade = "F"

print("Grand: ", grade)