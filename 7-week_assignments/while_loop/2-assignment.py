# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
count = 0
i = 0

# Needed Output
while i < len(friends):
    if friends[i][0].islower():
        count += 1
        i += 1
        continue

    print(friends[i])
    i += 1

print(f"Friends Printed And Ignored Names Count Is {count}")
