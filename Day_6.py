"""
The game of hangman
-------------------
Game Start and the menu is printed.
The word is randomly selected from a list.
Create blanks for word length.
Ask for a guess from the player selecting one letter.
Check for letter in word.
Check if correct: Yes, add letter to board; No, add hangman piece.
Check if blanks are all filled in: Yes, you win; No, back to start.
Check if player has remaining lives: Yes, you lose; No, back to start
-------------------
"""

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []

print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
    display.append('_')

print(display)

guess = input("Guess a letter: \n").lower()

for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = letter
print(display)




