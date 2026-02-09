#1
class per():
    def __init__(self,name):
        self.name = name 
    def greet(self):
        print("Hello, My name is "+ self.name)
p1 = per("Aydyn")
p1.greet()

#2
class calc():
    def add(self,a,b):
        return a + b
    def mult(self,a,b):
        return a * b
    def min(self,a,b):
        return a - b
    def div(self,a,b):
        return a / b
cal = calc()
print(cal.add(4,4))
print(cal.mult(4,5))
print(cal.min(9,11))
print(cal.div(14,7))

#3
class person2():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def mess(self):
        return f"{self.name} is {self.age} years old."
p2 = person2("Maral",16)
print(p2.mess())

#4
class person3():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def birthday(self):
        self.age += 1
        print(f"Happy birthday! you are now {self.age}!")
p3 = person3("Aydyn",17)
p3.birthday()

