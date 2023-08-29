account_balance = 1000

def Withdraw(amount):
    global account_balance
    if amount <= 0:
        print("invalid number please enter the correct value")
    elif amount > account_balance:
        print("amount is larger than account balance")
    else:
        account_balance -= amount
        print(f"{amount} is withdrwa successfully")

def deposit(amount):
    global account_balance
    if amount <= 0:
        print("invalid number please enter correct value")
    else:
        account_balance += amount
        print(f"{amount} has been added to your account")

def checkBalance():
  print(f"Your account balance is {account_balance}")

while True:
    print("Menu:")
    print("1.Withdrwal")
    print("2.Deposit")
    print("3.CheckBalance")

    choice = int(input("enter your choice"))
    if choice == 1:
        am = int(input("please enter amount you want to withdraw"))
        Withdraw(am)

    elif choice == 2:
        am1 = int(input("enter the amount you want to deposit"))
        deposit(am1)

    elif choice == 3:
        checkBalance()

    else:
        print("invalid choice")
        break


