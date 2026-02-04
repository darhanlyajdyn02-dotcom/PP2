#1
a = 65
b = 34
if a > b:
    print("a greater than b")
else:
    print("a does not greater than b")

#2
a = 8
b = 9
if a == b:
    print("a and b are equal")
else:
    print("a and b are not equal")

#3
a = int(input())
if a % 2 == 0:
    print("This is even")
else:
    print("This is odd")

#4
age = int(input("age: "))
if age >= 18:
    print("Welcome!")
else:
    print("You can not to come in")


#5
name = "Aydyn"
if len(name) > 0:
    print("Welcome!", name)
else:
    print("Error: Username cannot be empty")
