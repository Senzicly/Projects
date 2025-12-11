#12/9/25
#A program that can display a leaderboard, check information in the leaderboard
#It lets you pick a number (position) on the leaderboard and display all the names


import csv
import time

#Multi-purpose CSV file reader WORK ON THIS!!!!!!!!
def leaderboard(filename, rowIndex=None):
    with open(filename, mode='r', newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        csvList = list(reader)
        
        if (rowIndex == None):
            rows = csvList
        else:
            rows = csvList[rowIndex]
        value = rows
        return value



def hometown():
    a = " "
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("-                                               -")
    print("*                  HOMETOWNS                    *")
    print("-  (O) - Orlando                                -")
    print("*  (J) - Jacksonville                           *")
    print("-  (T) - Tampa/Tallahassee                      -")
    print("*  (M) - Miami                                  *")
    print("-  (S) - St. Petersburg                         -")
    print("*  (C) - Cape Coral                             *")
    print("-  (F) - Fort Lauderdale                        -")
    print("*  (P) - Port St. Lucie                         *")
    print("-                                               -")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    return a
    
    
    
def commands():
    a = " "
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("-                                               -")
    print("*                  COMMANDS                     *")
    print("-                                               -")
    print("* (H) - Search by Hometown                      *")
    print("- (R) - Search by Rank                          -")
    print("* (L) - Display the entire leaderboard          *")
    print("-                                               -")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    return a

    
    

def main():
    
    print("...")
    time.sleep(2)
    
    print("Welcome to 'gamerboard.com', home to the leaderboard of gamers!")
    print("Here, you can find a leaderboard of the top 50 gamers in all of the United States.")
    print("A prompt will appear so you can filter through it, happy searching!")
    time.sleep(2)
    print(" ")
    
    print(commands())
    
    command = input("Enter letter: ").lower()
    time.sleep(1)
    
    if (command == "h"):
        print(hometown())
        
        townCommand = input("Enter Hometown Letter: ")
        print(leaderboard("battle_royale.csv", townCommand))
        
    

    
    #For specific positions, I can just print the row
    #For the entire leaderboard, I can just print it, I need to figure out how to format it though.
    #Okay, we search by rank and hometown, lets make a menu for the hometowns
    

main()


