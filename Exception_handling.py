# a = int(input("enter the number"))
# try:
#     print(a)
# except:
#     print('invalid input')
z = input("enter the number")
try:
    a/b
    print("Multiplication of two number", {int(a)*int(a)})
except NumError:
    print('invalid number')
else:
    print("nothing went wrong")
finally:
    print()