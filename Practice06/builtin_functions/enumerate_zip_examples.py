list1 = ["a","b","c","d","e","f","g","h"]
list2 = [1,2,3,4,5,6,7,8]

for ix, val in enumerate(list1):
    print(f"{ix}:{val}", end = " ")
print()

for char, num in zip(list1, list2):
    print(f"{char}-{num}", end = " ")
print()
    