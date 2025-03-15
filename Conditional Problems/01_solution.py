#Problem: Classify a person's age group: Child(< 13), Teenager(13-19), Adult(20-59), Senior(60+)

age = 62
if age>0:
    if age<13:
        print("Child")
    elif age<20:
        print("Teenager")
    elif age<60:
        print("Adult")
    else:
        print("Senior")
else:
    print("Enter a number from 1 to 100!")