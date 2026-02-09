#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#2
nums = [-10, 5, -3, 2]
result = sorted(nums, key=lambda x: x)
print(result)

#3
words = ["apple", "hi", "banana", "cat"]
result = sorted(words, key=lambda x: len(x))
print(*result)

#4
data = [(1, 5), (2, 1), (3, 3)]
result = sorted(data, key=lambda x: x[1])
print(result)

#5
words = ["apple", "banana", "cherry"]
result = sorted(words, key=lambda x: x[-1])
print(result)

#6
nums = [5, 1, 9, 3]
result = sorted(nums, key=lambda x: x, reverse=True)
print(result)
