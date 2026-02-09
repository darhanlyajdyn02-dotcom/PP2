#1
a = lambda x: x ** 2
print(a(10))

#2
mult = lambda x,y: x * y
print(mult(4,5))

#3
summ = lambda a,b,c,d: a + b + c + d
print(summ(9,9,9,9))

#4
def myfun(n):
    return lambda a : a * n
v1 = myfun(2)
print(v1(10))

#5
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(12))
