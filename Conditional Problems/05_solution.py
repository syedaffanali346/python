#Problem: Check if a password is "weak", "medium" or "strong". Criteria: <6 chars (week), 6-10 chars (medium), >10 chars (strong).

password = "12"
lenOfPass = len(password)
if lenOfPass<6:
    strenth = "Week"
elif lenOfPass<=10:
    strenth = "Medium"
else:
    strenth = "Strong"

print("Password strenth: ",strenth)