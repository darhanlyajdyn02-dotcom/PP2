#1
def func(x,y,z):
    return x + y - z
print(func(4,4,8))

#2
def fun(name):
    return name + " Hey!"
print(fun("Aidyn"))

#3
def function(a, b, /, *, c, d):
  return a + b + c + d

res = function(5, 10, c = 15, d = 20)
print(res)

#4
def rule(a,b):
    return (a+b)*(a-b)
print(rule(5,4))

#5
def power(a):
    return a ** 2
x = int(input())
print(power(x))