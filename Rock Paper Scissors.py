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
    
    #Game Preparation
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
        
        
        elif (you == "rock"):
            print(" ")
            if (enemy == "rock"):
                print("..shoot!")
                print("ENEMY chose " + you + " as well! Tie :O .")
                z=z+1
                
            if (enemy == "paper"):
                print("..shoot!")
                print("ENEMY chose " + enemy + ". Point to ENEMY :( .")
                y=y+1
                
            if (enemy == "scissors"):
                print("..shoot!")
                print("ENEMY chose " + enemy + ". Point to YOU :) .")
                x=x+1
            
            print(" YOU = " + str(x) + ", ENEMY = " + str(y) + ", TIES = " + str(z) + ".")
            
            
        elif (you == "paper"):
            if (enemy == "paper"):
                print("..shoot!")
                print("ENEMY chose " + you + " as well! Tie :O .")
                z=z+1
                
            if (enemy == "scissors"):
                print("..shoot!")
                print("ENEMY chose " + enemy + ". Point to ENEMY :( .")
                y=y+1
                
            if (enemy == "rock"):
                print("..shoot!")
                print("ENEMY chose " + enemy + ". Point to YOU :) .")
                x=x+1
            
            print(" YOU = " + str(x) + ", ENEMY = " + str(y) + ", TIES = " + str(z) + ".")
            
            
        elif (you == "scissors"):
            if (enemy == "scissors"):
                print("..shoot!")
                print("ENEMY chose " + you + " as well! Tie :O .")
                z=z+1
                
            if (enemy == "rock"):
                print("..shoot!")
                print("ENEMY chose " + enemy + ". Point to ENEMY :( .")
                y=y+1
                
            if (enemy == "paper"):
                print("..shoot!")
                print("ENEMY chose " + enemy + ". Point to YOU :) .")
                x=x+1
            
            print(" YOU = " + str(x) + ", ENEMY = " + str(y) + ", TIES = " + str(z) + ".")
    
        
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
