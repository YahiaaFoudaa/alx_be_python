# You will create two Python scripts: bank_account.py, 
# which contains the BankAccount class, 
# and main-0.py, which interfaces with the class 
# through command line arguments to perform banking operations.

#Define a class named 
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current balance is {self.account_balance}")
