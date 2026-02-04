#1
a = 9
b = 4
if a == b: print("a and b are equal")
elif a > b: print("a is greater than b")
else: print("b is greater than a")

#2
x = 2
y = 9
print("x is greater") if x > y else print("y is greater")

#3
a = 4
b = 3
big = a if a > b else b 
print("Bigger is:", big)

#4
a = 110
b = 110
print("Big is",a) if a > b else  print("They are equal") if a == b else print("Big is",b)

#5
name = str(input("Name: "))
dname = name if name else "Guest"
print("Welcome!", dname)
