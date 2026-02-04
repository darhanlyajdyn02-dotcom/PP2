#1
print(2 < 3) # True
print(2 == 8) #False
print(9 > 1) # True

#2
a = 4
b = 8
if a > b:
    print("a greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b greater than a")

#3
print(bool("Hi, Aydyn")) #True
print(bool(4321)) #True

#4
print(bool(0)) #False
print(bool([])) #False
print(bool({})) #False
print(bool("")) #False

#5
a = "KBTU"
b = 999
c = ""
print(bool(a),bool(b),bool(c)) # True True False