#1
for i in range(16):
    if i % 2 == 0:
        continue
    print(i,end = " ")  # only odd numbers
print()
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print()

#3
words = ["cat", "elephant", "dog", "giraffe"]
for w in words:
    if len(w) < 5:
        continue
    print(w)
print()

#4
num = 7
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")
print()

#5
nums = [2,4,6,8,2,4,6,9,8]
for n in nums:
    if n % 2 != 0:
        print("found odd number:", n)
        break
else:
    print("all numbers are even")

#6
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

