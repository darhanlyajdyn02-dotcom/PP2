#1
n = int(input())
def func(n):
    for i in range(1,n+1):
        yield i**2
for x in func(n):
    print(x, end = " ")
print()


#2
n = int(input())
def even(n):
    for i in range(0,n+1,2):
        yield i
print(*even(n), sep = ",")
print()

#3
n = int(input())
def div(n):
    for i in range(0,n+1,12):
        yield i
print(*div(n), sep = " ")
print()

#4
a,b = map(int,input().split())
def squ(a,b):
    for i in range(a,b+1,1):
        yield i**2
print(*squ(a,b))

#5
n = int(input())
def fun(n):
    for i in range(n,-1,-1):
        yield i
print(*fun(n))
print(type(fun(n)))
print()
