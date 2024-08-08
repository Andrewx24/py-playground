class Math: 
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    def modulus(self):
        return self.a % self.b
    
class  Math2(Math):
    def __init__(self,a,b):
        super().__init__(a,b)
    def add(self):
        return self.a + self.b + 10
    def multiply(self):
        return self.a * self.b + 10
x= Math(10, 5)
x2= Math2(10, 5)
print(x.add())
print(x.multiply())
print(x2.add())


def name():
    print("Hello, my name is John")
    def greet():
        print("Hello, my name is John")

print(name())