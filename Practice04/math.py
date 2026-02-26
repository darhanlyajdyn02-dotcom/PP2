import math

#1
n = int(input())
rad = n * (math.pi/180)
print(round(rad,6))

#2
h,a,b = map(int,input().split())
area = (a+b)*h/2
print(area)

#3
side,length = map(int,input().split())
areap = (side * length**2)/(4 * math.tan(math.pi/side))
print(round(areap))

#4
length,height = map(int,input().split())
parallel = length * height
print(parallel)