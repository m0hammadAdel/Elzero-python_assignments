def calculate(num1, num2, op = 'a'):
    if op.lower() == 'add' or op[0].lower() == 'a':
        return num1 + num2
    
    elif op.lower() == 'subtract' or op[0].lower() == 's':
        return num1 - num2
    
    elif op.lower() == 'multiply' or op[0].lower() == 'm':
        return num1 * num2

# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200