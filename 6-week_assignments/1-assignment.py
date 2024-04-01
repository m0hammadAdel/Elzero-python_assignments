# Inputs

num1 = int(input("Please Enter the First Number: "))
num2 = int(input("Please Enter the First Number: "))
operation = input("Enter The Operation: + Or - Or * Or / Or %: ").strip()

# Needed Output

if operation == '+':
    print(f"{num1} {operation} {num2} = {num1 + num2}")

elif operation == '-':
    print(f"{num1} {operation} {num2} = {num1 - num2}")

elif operation == '*':
    print(f"{num1} {operation} {num2} = {num1 * num2}")

elif operation == '/':
    print(f"{num1} {operation} {num2} = {num1 / num2}")

elif operation == '%':
    print(f"{num1} {operation} {num2} = {num1 % num2}")

else:
    print("You entered a wrong operation.")