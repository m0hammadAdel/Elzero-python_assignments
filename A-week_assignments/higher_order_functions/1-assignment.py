friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

new_friends = list(map(lambda friend: friend[1:] , friends_map))

for friend in new_friends:
    print(friend)

# Output
"Eman"
"Ahmed"
"Sameh"
"Osama"