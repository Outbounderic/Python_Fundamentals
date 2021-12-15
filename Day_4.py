import random

# random number generator -> assign to elements
# conditional logic for what beats what

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_choice = [rock, paper, scissors]
random_num = random.randint(0, (len(game_choice) - 1))
computer_throw = random_num
computer_choice = game_choice[computer_throw]

# rock beats scissors
# scissors beats paper
# paper beats rock

player_throw = int(input("What do you choose? Type: 0 for Rock, 1 for Paper, or 2 for Scissors."))
player_choice = game_choice[player_throw]
print("The computer: \n" + computer_choice)
print("The player: \n" + player_choice)

if player_throw == computer_throw:
    print("It's a tie try again.")
elif player_throw != computer_throw:
    if player_throw == 0 and computer_throw == 1:
        print("The computer has won!")
    elif player_throw == 0 and computer_throw == 2:
        print("You have won!")

    if player_throw == 1 and computer_throw == 0:
        print("You have won!")
    elif player_throw == 1 and computer_throw == 2:
        print("The computer has won!")

    if player_throw == 2 and computer_throw == 0:
        print("The computer has won!")
    elif player_throw == 2 and computer_throw == 1:
        print("You have won!")



