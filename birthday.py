import datetime

# ask for the user's name
name = input("What is your name? ")

# ask for the user's birth month
birth_month = input("What month were you born in? ")

# get the current month
now = datetime.datetime.now()
current_month = now.strftime("%B")

# print a greeting using the user's name
print(f"Hello, {name}!")

# print the number of letters in the user's name
print(f"Your name has {len(name)} letters.")

# check if the user's birth month is the current month
if birth_month.lower() == current_month.lower():
    print("Happy birthday month!")  