import re

# #1
s = input()
p = r"^(ab)*$"

if re.match(p,s):
    print("Yes")
else:
    print("No")

# #2
s = input()
p = r"^(ab)*$"
if re.match(p,s):
    print("Yes")
else:
    print("No")

# #3
text = input()
p = r"\b[a-z]+_[a-z]+\b"
res = re.findall(p,text)
print(res)

#4
text4 = input()
p4 = r"\b[A-Z][a-z]+\b"
res4 = re.findall(p4,text4)
print(res4)

#5
s5 = input()
p5 = r"^.*ab$"
if re.match(p5,s5):
    print("Yes")
else:
    print("No")

#6
text6 = input()
res = re.sub(r"[ ,.]",":",text6)
print(res)

#7
text7 = input()
def func(text7):
    return re.sub(r"_([a-z])",lambda x:x.group(1).upper(),text7 )
print(func(text7))

#8
text8 = input()
res = re.findall(r"[A-Z][a-z]*",text8)
print(res)

#9
text9 = input()
res = re.sub(r"([A-Z])",r" \1",text9)
print(res)

#10
text10 = input()
res = re.sub(r"([A-Z])",r"_\1",text10).lower()
print(res)