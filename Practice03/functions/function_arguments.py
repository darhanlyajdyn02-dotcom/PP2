#1
def myfun(name):
    print(name + ", Welcome!")
myfun("Aydyn")
myfun("Azamat")
myfun("Nurda")

#2
def myfunc(name1,name2):
    print(name1 + " and " + name2)
myfunc("Aydyn","Ali")

#3
def func(name = "friend"):
  print("Hello", name)

func("Emil")
func()

#4
def funct(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

funct("dog","Bob")

#5
arr = ["apple","banane","chery","waterm"]
def frut(arr):
  for x in arr:
    print(x,end = " ")
frut(arr)
frut(arr)
print()

#6
def ffun():
  return (15,32)
a,b = ffun()
print(a,b)

#7
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[2])
print(fruits[1])
print(fruits[0])

#8
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")