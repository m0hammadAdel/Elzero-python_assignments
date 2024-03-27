nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

print(nums | letters) # {1, 2, 3, "A", "B", "C"}
print(nums.union(letters)) 
# {1, 2, 3, "A", "B", "C"}
nums.update(letters)
print(nums) # {1, 2, 3, "A", "B", "C"}