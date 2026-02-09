#1
nums = [1,2,3,4,5,6]
multt = list(map(lambda x: x * 2,nums))
print(*multt)

#2
nums2 = [3,4,5,6,7,8]
power = list(map(lambda x : x ** 2,nums2))
print(*power)

#3
arr = list(map(int,input().split()))
mul = list(map(lambda x : x * 3,arr))
print(*mul)

#4
arr = list(map(int,input().split()))
def func(*ar):
    pow = list(map(lambda x: x**2,arr))
    return pow

print(*func(arr))
