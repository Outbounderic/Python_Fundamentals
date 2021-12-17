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

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
count = 0
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
    count += 1

while count > 0:
    guess = input("Guess a letter: \n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            count -= 1
    print(display)
        





