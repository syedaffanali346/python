# Encapsulation

class Account:
    # Constructor
    def __init__(self, name, balance, account):
        self.name = name
        self.balance = balance
        self.amount = account

    # Debit Method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited!")
        print("Total balance is", self.get_balance())

    # Credit Method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited!")
        print("Total balance is", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account("Zakir", 10000, 12345)
acc1.credit(500)
acc1.debit(800)
