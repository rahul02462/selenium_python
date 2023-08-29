# a = "bannana"
# for i in a:
#     print(i)
# def myFunction(a):
#     if(a == 'rahul'):
#         print("hi the entered name is rahul")
# myFunction('rahul')
# for i in range(1,11):
#     print(i)
a = input("enter the number")
print(f"Multiplication table of {a} is following")
for i in range(1,11):
    print(f"{int(a)}X{i} = {int(a)*int(i)}")
