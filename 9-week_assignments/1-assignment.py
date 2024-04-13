import os

try:
    # the working directory has to be the whole assignments
    open('9-week_assignments/python/Our_file.py','x')
except IOError:
    print("The file cannot be created")

for i in range(50):
    try:
        # the working directory has to be the whole assignments
        open('9-week_assignments/python/txt{i}.txt','x')
    except IOError:
        print("The file cannot be created")


f = open('9-week_assignments/python/txt1.txt', 'r')

