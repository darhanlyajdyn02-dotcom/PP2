
import datetime

#1
today = datetime.datetime.now()
res = today - datetime.timedelta(days = 5)
print(res)
print()

#2
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday)
print(today)
print(tomorrow)
print()

#3
today = datetime.datetime.now()
mic = today.replace(microsecond = 0)
print(mic)
print()

#4
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
diff = today - yesterday
sec = diff.total_seconds()
print(sec)
