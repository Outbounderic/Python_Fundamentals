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

end_of_game = False
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: \n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")
        
#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    print(f"{' '.join(display)}")  

    if "_" not in display:
        end_of_game = True
        print("You win!")


    print(stages[lives])
        
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.




