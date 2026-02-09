#1
nums = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x: x % 2 == 0,nums))
print(*even)

#2
nums2 = [1,2,3,4,5,6,7,8,9]
odd = list(filter(lambda x: x % 2 != 0,nums2))
print(*odd)

#3
num3 = [1,2,3,4,5,6,7,8,9]
div3 = list(filter(lambda x: x % 3 == 0,num3))
print(*div3)

#4
n = [1,2,3,4,5,6,7,8,9]
def div4(*arr):
    div = list(filter(lambda x: x % 4 == 0,n))
    return div
print(*div4(n))