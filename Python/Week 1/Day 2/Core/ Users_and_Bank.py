class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print(f"Balance:{self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:self.balance-=5
        print(f"Balance:{self.balance}")
    def display_account_info(self):
        print(f"Balance:{self.balance}")
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f"Balance:{self.balance}")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def 
    
    def make_deposit(self, amount):
        self.balance+=self.amount
