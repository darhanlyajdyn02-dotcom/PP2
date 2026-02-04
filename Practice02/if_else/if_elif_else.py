#1
x = 10
y = 10
if x > y:
    print("x greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("x is not greater than y")

#2
score = int(input())

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#3
a = 12
b = 13
if a > 10 or a == b:
    print("Yes, it fits")
elif b < a:
    print("No, it is not fits")

#4
day = int(input())

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#5
score = int(input())

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")

