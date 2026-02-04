#1
numbers = [1, 3, 5, 8, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number is {num}")
        break
print()

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print()

#3
nums = [4, 7, 2, -1, 5]
for n in nums:
    if n < 0:
        print("Negative number:", n)
        break
print()

#4
word = "python"
for x in word:
    if x == 'h':
        print("found h")
        break
print()

#5
a = 21
for i in range(a):
    if i == 20:
        break
    print(i,end = " ")
print()

