# class myClass:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def fullName(self):
#         y = format(self.age)
#         print("hello my name is:"+self.name + "And age is :" + y)
#
# p1 = myClass('rahul',28)
# p1.fullName()

class myClass:
    def __init__(self,age,name):
        self.name = name
        self.age = age

    def Person(self):
        print(self.name,self.age)

p1 = myClass('rahul',28)
p1.Person()