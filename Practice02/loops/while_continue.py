#1
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()

#2
i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=' ') # 1,2,4,5,7,8,10
    i += 1
print()

#3
i = 1
while i <= 20:
    if i % 5 == 0:
        i += 1
        continue
    print(i, end=' ')
    i += 1
print()

#4
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print()

#5
s = "a1b2c3df!"
i = 0
while i < len(s):
    if not s[i].isalpha():
        i += 1
        continue
    print(s[i], end='')
    i += 1


