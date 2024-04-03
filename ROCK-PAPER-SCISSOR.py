# AUTHOR:- KUSH SHAH
import random

print("Welcome to the Rock, Paper, Scissors game!")
print("Enter 0 for scissors, 1 for rock, 2 for paper")
while True:
    user = int(input("Enter your choice: "))
    computer = random.randint(0, 2)
    print("The choise of computer is",computer)
    
    if user > 2 or user < 0:
        print("Invalid choice!")
        continue

    if user == computer:
        print("Tie!")
    elif user == 0 and computer == 1:
        print("You lose!")
    elif user == 1 and computer == 2:
        print("You lose!")
    elif user == 2 and computer == 0:
        print("You lose!")
    else:
        print("You win!")
    
    if input("Do you want to play again? (y/n): ") == "n":
        break
