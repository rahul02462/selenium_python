class Person:
    def __init__(self,age,name):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"My name is {self.name} and I am {self.age} older"

class Student(Person):
    def __init__(self,age,name,grade):
        super().__init__(name,age)
        self.grade = grade

    def say_hello(self):
        return f"My name is {self.name} and I am {self.age} older and my grade is {self.grade}"

Person1 = Person("Rahul",28)
Person2 = Student("Sharma",28,'A')

print(Person2.say_hello())