"""
Create a bank account class that has attributes "owner", "balance" and two methods "deposit" and "withdraw".
Withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
        print(f"Operation successfull: deposit {money}\nYour balance: {self.balance}")

    def withdraw(self, money):
        if self.balance - money >= 0:
            self.balance -= money
            print(f"Operation successfull: withdraw {money}\nYour balance: {self.balance}")
        else:
            print(f"Operation impossible: You don't have {money} in your balance\nYour balance: {self.balance}")

p1 = Account("Galek", 50000)

p1.deposit(75000)

p1.withdraw(100000)

p1.withdraw(100000)