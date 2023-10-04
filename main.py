"""
LEVEL : B E G I N N E R.
-----------------------------------------------------------
Project - Rock Paper Scissor Game.✌️✊✋
-----------------------------------------------------------
Module:
* random - random is a built-in module of the Python programming language. It is used to generate pseudorandom numbers.

Functions Used:
* Print - Prints a string into the console. || ex: print("Hello World").
* Input - Prints a string into the console, and asks the user for a string input. || ex: name = input("What's your name").

Conditional Statement:
* if-elif-else
"""

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

import random
choice = input("|for rock-0 , paper-1 , scissors-2|Please enter your choice: ")
P_choice = int(choice)
C_choice = random.randint(0,2)
if P_choice == 0 and C_choice == 0:
    print("Your Choice : ")
    print(rock)
    print("Computer Choice : ")
    print(rock)
    print("You Tied.")
elif P_choice == 0 and C_choice == 1:
    print("Your Choice : ")
    print(rock)
    print("Computer Choice : ")
    print(paper)
    print("You Lose.")
elif P_choice == 0 and C_choice == 2:
    print("Your Choice : ")
    print(rock)
    print("Computer Choice : ")
    print(scissors)
    print("You Won.")
elif P_choice == 1 and C_choice == 0:
    print("Your Choice : ")
    print(paper)
    print("Computer Choice : ")
    print(rock)
    print("You Won.")
elif P_choice == 1 and C_choice == 1:
    print("Your Choice : ")
    print(paper)
    print("Computer Choice : ")
    print(paper)
    print("You Tied.")
elif P_choice == 1 and C_choice == 2:
    print("Your Choice : ")
    print(paper)
    print("Computer Choice : ")
    print(scissors)
    print("You lose.")
elif P_choice == 2 and C_choice == 0:
    print("Your Choice : ")
    print(scissors)
    print("Computer Choice : ")
    print(rock)
    print("You Lose.")
elif P_choice == 2 and C_choice == 1:
    print("Your Choice : ")
    print(scissors)
    print("Computer Choice : ")
    print(paper)
    print("You Won.")
else :
    print("Your Choice : ")
    print(scissors)
    print("Computer Choice : ")
    print(scissors)
    print("You Tied.")