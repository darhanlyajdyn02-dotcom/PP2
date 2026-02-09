class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Gav gav"

class Cat(Animal):
    def make_sound(self):
        return "Mweo mweo"

animal = Animal()
dog = Dog()
cat = Cat()

print(animal.make_sound())  
print(dog.make_sound())     
print(cat.make_sound())     