# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse = True)
i = 1

# Needed Output
for num in my_nums:
    if num % 5 == 0:
        print(f"{i} => {num}")

print("All Numbers Printed")