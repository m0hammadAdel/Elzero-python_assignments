# ----------- functions -----------
def my_all(my_nums):
    for num in my_nums:
        if not num:
            return False

    return True

def my_any(my_nums):
    for num in my_nums:
        if num:
            return True

    return False

def my_min(my_nums):
    min = 0

    for num in my_nums:
        if min > num:
            min = num

    return min

def my_max(my_nums):
    max = 0

    for num in my_nums:
        if max < num:
            max = num

    return max

# ----------- output -----------
# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700