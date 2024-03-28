# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

# Needed Output
if country in countries:
    print("Your Country Eligible For Discount And The Price After Discount Is $70") # Egypt Example
else:
    print("Your Country Not Eligible For Discount And The Price Is $100") # Ghana Example