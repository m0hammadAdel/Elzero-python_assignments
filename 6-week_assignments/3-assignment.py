# Input
age = int(input("Please Enter Your Age: "))

# Needed Output
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if age < 100 and age > 10:
    print(f"Your Age In Months Is {months} months")
    print(f"Your Age In Weeks Is {weeks} week")
    print(f"Your Age In Days Is {days} days")
    print(f"Your Age In Hours Is {hours} hour")
    print(f"Your Age In Minutes Is {minutes} minutes")
    print(f"Your Age In Seconds Is {seconds} seconds")

else:
    print("You either is too young to use a machine like that or too old to even breathe")