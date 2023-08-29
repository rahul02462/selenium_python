class BankAccount:
    def __init__(self,balance,acocunt_number):
        self.balance = balance
        self.account_number = acocunt_number

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self):
        return self.balance

obj = BankAccount(45,'1213')
print(obj.deposit)
