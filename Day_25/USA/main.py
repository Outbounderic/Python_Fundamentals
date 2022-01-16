import turtle
import pandas
from guess import Guess

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess = Guess()
game_is_on = True
correct_guesses = []
score = 0
lives = 5

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
coord_list_x = data["x"].to_list()
coord_list_y = data["y"].to_list()

while game_is_on:
    answer_state = screen.textinput(title=f"Guess the state.\nLives: {lives}", prompt=f"What's another states name?\nLives: {lives}").title()

    if len(correct_guesses) == len(state_list):
        print("Congratulations! You know your states!")
        game_is_on = False
    elif answer_state in state_list:
        state_index = state_list.index(answer_state)
        guess.add_guess(answer_state, (coord_list_x[state_index], coord_list_y[state_index]))
        correct_guesses.append(answer_state)
        score += 1
    else:
        lives -= 1
        if lives == 0:
            print("Looks Like you need to study your states.")
            game_is_on = False

if not game_is_on:
    print(f"Correct Guesses: {score}")
    print(f"Correct States: {correct_guesses}")
    exit()

turtle.mainloop()
