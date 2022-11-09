import random

game_state = True
word_list = ["ardvark", "baboon", "camel"]
display = []
lives = ["x", "x", "x"]
chosen_word = word_list[random.randint(0, (len(word_list) - 1))]

for _ in chosen_word:
    display.append("_")

while game_state != False:
    print(f"Current Guess: {display} \nLives remaining: {lives}")
    guess = input(f"Guess a letter from a - z : ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
    
    if guess not in chosen_word:
        lives.pop()

    if "_" not in display:
        game_state = False
        print("Congrats")
    elif "x" not in lives:
        game_state = False
        print("So sorry")
