import turtle
import pandas
from guess import Guess
PATH = "./Player Logs/"

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess = Guess()
correct_guesses = []
score = 0

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
coord_list_x = data["x"].to_list()
coord_list_y = data["y"].to_list()

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"Guess the state.", prompt=f"What's another states name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(PATH+f"states_to_learn.csv")
        break
    elif answer_state in state_list:
        state_index = state_list.index(answer_state)
        guess.add_guess(answer_state, (coord_list_x[state_index], coord_list_y[state_index]))
        correct_guesses.append(answer_state)
        score += 1



