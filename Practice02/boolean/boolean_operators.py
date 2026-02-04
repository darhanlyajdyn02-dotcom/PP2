#1
x = 10
print( x > 5 and x < 15) #True
print(x > 12 and x < 8) #False

#2
def func():
    return True
if func():
    print("Yes")
else:
    print("No")

#3
a = 3
b = 8
def equal():
    if a + 5 == b:
        return True
    else:
        return False
if equal():
    print("Yes")
else:
    print("No")

#4
a = 2 
b = 5
print(a > 0 or b < 10)
print(a > 3 or b == 5)

#5
a = 9
b = 4
print(a > 11 or b < 3)