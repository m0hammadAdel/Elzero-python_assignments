# Input
num = 0

while num < 5:
    num = int(input("Please Enter A Number Greater than 5: "))

    if not isinstance(num, int) or num < 5:
        print("Wrong input Please Try Again!")
        continue

# Needed Output
"Number 0 Is Not Larger Than 0"

while num > 1:
    num -= 1
    
    if num == 6:
        continue

    print(num)