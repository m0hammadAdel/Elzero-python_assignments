my_set = {1, 2, 3}

# Needed Output

print(my_set) # {1, 2, 3}

my_set.clear()
print(my_set) # set()

my_set.add('A')
my_set.add('B')
print(my_set) # {"A", "B"}

my_set.discard('D')