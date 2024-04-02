# Input
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

# Needed Output
for subj, grade in my_ranks.items():
    if grade == 'A':
        num_grade = 100
    elif grade == 'B':
        num_grade = 80
    elif grade == 'C':
        num_grade = 40
    else:
        print("There is an Invalid grade.")
        break

    print(f"My Rank in {subj} Is {grade} And This Equal {num_grade} Points")   