def show_skills(name, *skills):
    if skills:
        print(f"Hello {name.capitalize()} Your Skills Are:")

        for skill in skills:
            print(f"- {skill}")
    
    else:
        print(f"Hello {name.capitalize()} You Have No Skills To Show")


# Input
show_skills("Osama", "HTML", "CSS", "JS", "Python")

# Output
"Hello Osama Your Skills Is"
"- HTML"
"- CSS"
"- JS"
"- Python"

# Input
show_skills("Ahmed")

# Output
"Hello Ahmed You Have No Skills To Show"