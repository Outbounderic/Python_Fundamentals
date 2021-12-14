print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

# input -> conditional 2
# input -> conditional 2
# input -> condiiional 4

print("You reach a coast; you can go around through the treacherous jungle or you can take your time and swim.")
first_choice = input('Jungle or Swim ').lower()

if first_choice == 'jungle':
    print("As you hike through the jungle you trip on a hidden branch and fall in to a hole. \nGame Over.")
    exit()
elif first_choice == 'swim':
    print("You take your time and swim, the sun is perfect and water is clear. You see a school of fish ahead.")
    second_choice = input('Swim or Wait ').lower()
    if second_choice == 'swim':
        print('As you swim through the school of fish you are attacked by a shark. \nGame Over.')
        exit()
    elif second_choice == 'wait':
        print('You wait and are rewarded for your patience. A shark swims through the school looking for a snack. It passes and you make it to the shore.')
        print('You trek through the jungle for hours until you come across three stone doors.')
        third_choice = input('Which do you choose: Red, Blue, or Yellow. ').lower()
        if third_choice == 'red':
            print('As you walk into the red door you fall into a pit of fire. \nGame Over')
            exit()
        elif third_choice == 'blue':
            print('Passing the blue door it slams shut, several tigers attack you. \nGame Over')
            exit()
        elif third_choice == 'yellow':
            print('Walking past the yellow door you are greeted with a magnificent chest! \nYou Win!')
        else:
            print('After this long day no one blames you from turning around. \nGame Over')