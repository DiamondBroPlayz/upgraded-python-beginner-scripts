# Check if requirements are met
# If your looking for the explanation go to the other file

try:
    import datetime
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'datetime'])

# Fulfill requirements

from datetime import date

# Variables

today = date.today()
year = today.year

# Start

# Asking for user input:
while True:
    try:
        birth_year = int(input('What is your birth year? '))
        if birth_year > year:
            print("Your birth year cannot be in the future.")
            continue
        elif birth_year < 1900:
            print("Your birth year is too far in the past.")
            continue
        break
    except ValueError:
        print("Please enter a valid birth year.")

# Doing the math:
age = year - birth_year

# Printing results
if age == 0:
    print("Happy birthday! You are 0 years old today.")
else:
    print(f"Happy birthday! You are {age} years old today.")
