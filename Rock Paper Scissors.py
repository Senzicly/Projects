#Luis D.
#Rock Paper Scissors "Bot"



import random

def display_instructions():
    print("Hello there! I am your personal Rock-Paper-Scissors bot, or RPS.")
    print("I am here to play Rock Paper Scissors with you, obviously!")
    print("\n------------------------------------------------------------")
    print('"rock" means Rock')
    print('"paper" means Paper')
    print('"scissors" means Scissors')
    print('"quit" means to quit the game')
    print("Type rock, paper, or scissors when it starts")
    print("Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("------------------------------------------------------------\n")


def determine_winner(you, enemy):
    if you == enemy:
        return "tie"
    elif (you == "rock" and enemy == "scissors") or \
         (you == "scissors" and enemy == "paper") or \
         (you == "paper" and enemy == "rock"):
        return "you"
    else:
        return "enemy"


def main():
    # Display Instructions
    display_instructions()
    
    # Initialize Variables
    choices = ["rock", "paper", "scissors"]
    you_score = enemy_score = ties = 0
    
    # Game Loop
    while True:
        you = input("rock, paper, scissors.. ").lower()
        
        # Quit condition
        if you == "quit":
            break
        
        if you not in choices:
            print("Huh? Invalid choice. Try again!")
            continue

        # Random choice for enemy
        enemy = random.choice(choices)
        print("..shoot!")
        print(f"ENEMY chose {enemy}.")

        # Determine the winner
        result = determine_winner(you, enemy)
        
        if result == "tie":
            print("It's a tie :O .")
            ties += 1
        elif result == "you":
            print("Point to YOU :) .")
            you_score += 1
        else:
            print("Point to ENEMY :( .")
            enemy_score += 1

        # Show Scores
        print(f" YOU = {you_score}, ENEMY = {enemy_score}, TIES = {ties}.")
        print(" ")

    # Final Scores
    print("---------------")
    print("|   POINTS    |")
    print(f"|(YOU) = {you_score}     |")
    print(f"|(ENEMY) = {enemy_score}   |")
    print(f"|(TIES) = {ties}      |")
    print("---------------")
    print("Thank you for playing with me <3")


main()
