

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    def greet(self):
        print(f"Hello, my name is {self.name}")
        
    
x= Person("John", 36)

print(x.greet())
print(x.name)
print(x.age)

def sum (a, b):
    return a + b

a= sum(1, 2)
print(a)