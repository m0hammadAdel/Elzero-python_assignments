import datetime

time_now = datetime.datetime.now()

print(time_now.strftime("%Y-%m-%d"))
print(time_now.strftime("%b %d. %Y"))
print(time_now.strftime("%d - %b - %Y"))
print(time_now.strftime("%d / %b / %y"))
print(time_now.strftime("%d / %B / %Y"))
print(time_now.strftime("%a, %d %B %Y"))