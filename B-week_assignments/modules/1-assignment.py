from random import randrange

rand10_50 = lambda: randrange(10, 50) # return number between 10 to 50
rand_even = lambda: randrange(2, 10, 2) # return an even number between 2 to 10
rand_odd = lambda: randrange(1, 9, 2) # return and odd number between 1 to 9

print(rand10_50())
print(rand_even())
print(rand_odd())

print(dir(randrange))