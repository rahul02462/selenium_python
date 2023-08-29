class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Details(self):
        return f"My name is {self.name} and I am {self.age} older"

obj = myclass("rahul sharma",28)
print(obj.Details())