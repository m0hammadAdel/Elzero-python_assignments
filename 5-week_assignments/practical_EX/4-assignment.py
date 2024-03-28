# Inputs
email = input("Please Enter Your Email: ").strip().lower()

# Needed Output

print(f"Your Name Is {email[:email.index('@')].capitalize()}")
print(f"Email Service Provider Is {email[email.index('@') + 1: email.index('.')]}")
print(f"Top Level Domain Is {email[email.index('.') + 1:]}")