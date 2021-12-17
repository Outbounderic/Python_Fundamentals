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

#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, len(word_list)) - 1]
print(chosen_word)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.







