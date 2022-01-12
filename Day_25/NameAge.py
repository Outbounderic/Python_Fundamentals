from datetime import date

# Imported a module that keeps current year 
current_year = date.today()
user_name = input('What is your name? ')
user_age = input('What is your age? ')
birth_year = str(current_year.year - int(user_age))

# Using a newer type of string format
print(f'Hello {user_name}! You were born in {birth_year}')