def get_people_scores(name = "", **scores):
    if name:
        print(f"Hello {name.capitalize()}", end = " ")
    else:
        pass

    if scores:
        print("This Is Your Score Table:")
        for lang, grade in scores.items():
            print(f"{lang} => {grade}")

    else:
        print("You Have No Scores To Show")

# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"

# Test 3
get_people_scores(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"

# Test 4
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"