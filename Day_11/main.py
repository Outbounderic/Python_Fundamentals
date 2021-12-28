# Guess the number game with normal and hard modes
# Req input from player
# Compare if number is higher or lower than guess
# Res the state and decrement the amount of guesses left
# Loop over game cycle until guesses left equals zero or guess equals number

import random
guesses = 0
number_to_guess = random.randrange(1,101)

def set_difficulty(res):
    if res == "normal":
        return guesses + 10
    elif res == "hard":
        return guesses + 5

def compare_guess(res):
    if res == number_to_guess:
        print(f"That's correct the number is {number_to_guess}!")
        print("You win!")
        exit()
    elif res < number_to_guess:
        print(f"The number is higher than {res}.")
        return guesses - 1
    elif res > number_to_guess:
        print(f"The number is lower than {res}.")
        return guesses - 1

def game_loop():
    print("Welcome to the number guessing game. I'll pick a number and you will try to guess it, i'll let you know if you are above or below it.")
    guesses = set_difficulty(input("Would you like to play on normal or hard: "))

    while guesses > 0:
        compare_guess(int(input(f"Guess a number between 1 and 100: ")))
        guesses = guesses - 1
        print(f"You have {guesses} tries left.")
    
    if guesses == 0:
        print("You lose!")

game_loop()