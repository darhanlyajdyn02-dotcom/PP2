#1
def func(*names):
    print("First:",names[0])
    print("Second:",names[1])
    print("All anmes:", *names)
func("Aydn","Adik","Nurda","Aza")

#2
def funct(greeting, *names):
  for n in names:
    print(greeting, n)

funct("Hello", "Emil", "Tobias", "Linus")

#3
def total(*values):
    sum = 0
    for x in values:
        sum += x
    return sum
print(total(1,2,3,4,5,6,7,8,9))
print(total(1,1,1,1,1,1,1,1,1,1))
print()

#4
def maxval(*nums):
    max = nums[0]
    for x in nums:
        if x > max:
            max = x
    return max
print(maxval(3,2,5,7,4,2,5,8,9,6,5,0))

#5
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#6
def function(**var):
    print("Type:",type(var))
    print("Name:", var["name"])
    print("Age:",var["age"])
    print("Language:", var["lan"])
    print("All data:", var)
function(name = "Aidyn",lan = "Kazakh",age = "18")

#7
def my_function2(title,*args, **kwargs, ):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function2("User Info","Emil", "Tobias" ,age = 25, city = "Oslo")

#8
def sumv(a,b,c):
    return a + b + c 
arr = list(map(int,input().split()))
print(sumv(*arr))