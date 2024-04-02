# Input
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

# Needed Output
for student, courses in students.items():
    print("------------------------------")
    print(f"-- Student Name => {student}")
    print("------------------------------")
    final_degree = 0

    for subj, grade in courses.items():
        if grade == 'A':
            num_grade = 100
        elif grade == 'B':
            num_grade = 80
        elif grade == 'C':
            num_grade = 40
        elif grade == 'D':
            num_grade = 20

        print(f"- {grade} => {num_grade} Points")
        final_degree += num_grade

    print(f"Total Points For {student} Is {final_degree}")