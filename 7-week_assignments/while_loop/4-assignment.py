# Input
my_friends = []
max_num = 4
i = 0

# Algorithm
while max_num > 0:
    my_friends.append(input("Please Enter Next Name: "))

    if my_friends[i].isupper():
        print("Invalid Name")
        continue
    
    my_friends[i].capitalize()
    print(f"Friend {my_friends[i]} Added")
    print(f"Names Left in List Is {max_num - 1}")

    max_num -= 1
    i += 1