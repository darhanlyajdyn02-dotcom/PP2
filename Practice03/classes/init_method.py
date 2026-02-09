#1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Aydyn", 18)

print(p1.name)
print(p1.age)

#2
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

#3
class me:
  def __init__(self,name,age,city,country):
    self.name = name
    self.age = age
    self.city = city 
    self.country = country 
m1 = me("Aydyn",18,"Almaty","Kazahstan")
print(m1.name)
print(m1.age)
print(m1.city)
print(m1.country)

