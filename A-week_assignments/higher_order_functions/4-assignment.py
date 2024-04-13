skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

new_skills = list(filter( lambda skill: isinstance(skill, str), skills))
new_skills = list(reversed(new_skills))

skills_counter = enumerate(new_skills, 50)

for c, s in skills_counter:
    print(f"{c} - {s}")


# Output
"50 - JavaScript"
"52 - Python"
"53 - PHP"
"55 - CSS"
"56 - HTML"