import random
ROCK = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)   '''
PAPER ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)   '''
SCISSOR ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)   '''
game_images =[ROCK , PAPER , SCISSOR ]
users_choice = int(input("ENTER YOUR CHOICE : TYPE 0 FOR ROCK ; TYPE 1 FOR PAPER ; TYPE 2 FOR SCISSOR : "))

if users_choice >=3 or users_choice <0 :
    print("YOU ENTERED INVALID NUMBER , YOU LOOSE ")
else:
    print(game_images[users_choice])
    comp_choice = random.randint(0,2)
    print("COMPUTER CHOSE :")
    print(comp_choice)
    print(game_images[comp_choice])
    if users_choice==comp_choice :
        print ("ITS A DRAW ' YOU LOOSE")
    elif users_choice == 0 and comp_choice == 2:
        print("YOU WIN")

    elif comp_choice == 0 and users_choice == 2:
        print("YOU LOOSE")

    elif users_choice>comp_choice:
        print("YOU WIN")

    elif comp_choice>users_choice:
        print("YOU LOOSE")
