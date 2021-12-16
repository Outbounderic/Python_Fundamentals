#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# for loop
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_elements = []

for x in range(0, nr_letters):
    rand_letter = random.randint(1, (len(letters) - 1))
    password_elements.append(letters[rand_letter])

for x in range(0, nr_symbols):
    rand_symbols = random.randint(1, (len(symbols) - 1))
    password_elements.append(symbols[rand_symbols])

for x in range(0, nr_numbers):
    rand_numbers = random.randint(1, (len(numbers) - 1))
    password_elements.append(numbers[rand_numbers])

random.shuffle(password_elements)
print(f"\nYour password is: {''.join(password_elements)}.")
    