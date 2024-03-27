# Create Dictionary Here
my_dict = {
    "one" : {
        "lang" : "HTML",
        "progress" : "90"
    },
    "two" : {
        "lang" : "CSS",
        "progress" : "80"
    },
    "three" : {
        "lang" : "Python",
        "progress" : "30"
    }
}
# Needed Output

print(f"{my_dict["one"]["lang"]} progress is {my_dict["one"]["progress"]}%") 
print(f"{my_dict["two"]["lang"]} progress is {my_dict["two"]["progress"]}%") 
print(f"{my_dict["three"]["lang"]} progress is {my_dict["three"]["progress"]}%") 

my_dict["four"] = {
    "lang" : "AI",
    "progress" : "20"
}
print(f"{my_dict["four"]["lang"]} progress is {my_dict["four"]["progress"]}%") 