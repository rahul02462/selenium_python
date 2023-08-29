print("Welcome to simple Calculator")
print("1.Addition")
print("2.Subsctraction")
print("3.Multiplication")
print("4.Division")
a = input("Please enter the choice")
choice = input("please enter first number")
choice2 = input("please enter the second number")
if a == '1':
    print("Addition of two number is",int(choice)+int(choice2))
elif a == '2':
    print("Subsctraction of number is :",int(choice)-int(choice2))
elif a == '3':
    print("Multiplication of number is :", int(choice) * int(choice2))
elif a == '4':
    print("Division of number is :",int(choice)/int(choice2))
else:
    print("Invalid entry")
