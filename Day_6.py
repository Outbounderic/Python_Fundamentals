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




