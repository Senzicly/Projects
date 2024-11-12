#Luis
#11/10/24 - #11/11/24
#Rock-Paper-Scissors


def main():

    #Intro
    print("Hello there! I am your personal Rock-Paper-Scissors bot, or RPS.")
    print("I am here to play Rock Paper Scissors with you, obviously!")
    print("This is how you play the game.")
    
    print(" ")
    
    #Instructions
    print("------------------------------------------------------------")
    print('"rock" means Rock')
    print('"paper" means Paper')
    print('"scissors" means Scissors')
    print('"quit" means to quit the game')
    print(" ")
    print("Type rock, paper, or scissors when it starts")
    print("Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("------------------------------------------------------------")
    
    #Game Preperation
    import random
    list1=["rock", "paper", "scissors"]
    
    x=0
    y=0
    z=0

    you = " "

    while (you == "rock" or you == "paper" or you == "scissors" or you == "quit" or you == " "):
        print(" ")
        you = input("rock, paper, scissors.. ")
        enemy = random.choice(["rock", "paper", "scissors"])
        

        if (you == "quit"):
            break
        
        
        elif (you == "rock" and enemy == "rock"):
            print(" ")
            enemy = random.choice(["rock", "paper", "scissors"])
            print("..shoot!")
            print("You two tied! No point.")
            z=z+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))
            
        elif (you == "rock" and enemy == "paper"):
            print(" ")
            print("..shoot!")
            print("You lost :( Point for enemy!")
            y=y+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))

        elif (you == "rock" and enemy == "scissors"):
            print(" ")
            print("..shoot!")
            print("You won :) Point for you!")
            x=x+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))
            
            
        elif (you == "paper" and enemy == "rock"):
            print(" ")
            print("..shoot!")
            print("You won :) Point for you!")
            x=x+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))
        
        elif (you == "paper" and enemy == "paper"):
            print(" ")
            print("..shoot!")
            print("You two tied! No point.")
            z=z+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))
            
        elif (you == "paper" and enemy == "scissors"):
            print(" ")
            print("..shoot!")
            print("You lost :( Point for enemy.")
            y=y+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))


            
        elif (you == "scissors" and enemy == "rock"):
            print(" ")
            print("..shoot!")
            print("You lost :( Point for enemy.")
            y=y+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))
            
        elif (you == "scissors" and enemy == "paper"):
            print(" ")
            print("..shoot!")
            print("You won :) Point for you!")
            x=x+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))
            
        elif (you == "scissors" and enemy == "scissors"):
            print(" ")
            print("..shoot!")
            print("You two tied! No point.")
            z=z+1
            print("(YOU) = " + str(x) + " , (ENEMY) = " + str(y))
            
        
        else:
            print("Huh?")
            you = " "


    print("---------------")
    print("|   POINTS    |")
    print("|(YOU) = " + str(x) + "    |")
    print("|(ENEMY) = " + str(y) + "  |")
    print("|(TIES) = " + str(z) + "   |")
    print("---------------")
    
    print("Thank you for playing with me <3")

main()