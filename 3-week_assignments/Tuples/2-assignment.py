friends = ("Osama", "Ahmed", "Sayed")

# Needed Output
friends = list(friends)
friends[0] = "Elzero"
friends = tuple(friends)

print(friends) # ("Elzero", "Ahmed", "Sayed")
print(type(friends)) # <class 'tuple'>
print(len(friends)) # 3 Elements