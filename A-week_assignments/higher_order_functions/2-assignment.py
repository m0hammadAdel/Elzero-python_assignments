friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

new_friends = list(filter( lambda friend: friend[-1] == 'm', friends_filter))

for friend in new_friends:
    print(friend)

# Output
"Wessam"
"Essam"