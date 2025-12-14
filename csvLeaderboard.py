
#Luis Dacosta
#12/8/25
#A program that can display a leaderboard, check information in the leaderboard
#It lets you pick a number (position) on the leaderboard and display all the names


import csv
import time
from rich.console import Console
from rich.table import Table





#Multi-purpose CSV file reader
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





#Holds the Hometown commands
def hometown():
    a = " "
    print("***-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-***")
    print("*                                               *")
    print("*                  HOMETOWNS                    *")
    print("-  (O) - Orlando                                -")
    print("-  (J) - Jacksonville                           -")
    print("-  (T) - Tampa                                  -")
    print("-  (TA) - Tallahassee                           -")
    print("-  (M) - Miami                                  -")
    print("-  (S) - St. Petersburg                         -")
    print("-  (C) - Cape Coral                             -")
    print("-  (F) - Fort Lauderdale                        -")
    print("*  (P) - Port St. Lucie                         *")
    print("*                                               *")
    print("***-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-***")
    return a
    
    
    
    
    
    
#Holds the search commands    
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





#Uses __ to display the whole leaderboard as a cute table
def showLeaderboard(rows):
    console = Console()
    leadBoard = Table(title="Leaderboard", show_lines=True)
    leadBoard.add_column("-", justify="left", style="cyan", no_wrap=True)
    leadBoard.add_column("-", style="magenta")
    leadBoard.add_column("-", justify="right", style="green")
    leadBoard.add_column("-", style="yellow")

    for row in rows:
        leadBoard.add_row(*row)
    
    console.print(leadBoard)


    
#Main Code
def main():
    #Read CSV normally
    rows = leaderboard("battle_royale.csv")
    
    
    print("...")
    time.sleep(2)
    
    print("Welcome to 'gamerboard.com', home to the leaderboard of gamers!")
    print("Here, you can find a leaderboard of the top 50 gamers in all of the United States.")
    print("A prompt will appear so you can filter through it, happy searching!")
    time.sleep(2)
    print(" ")
    
    print(commands())
    
    #Decides what menu you get put into
    command = input("Enter letter: ").lower()
    time.sleep(1)
    
    #Hometown Search
    if (command == "h"):
        while True:
            print(hometown())
            
            townCommand = input("Enter Hometown Letter: ").upper()

            #Convert letter to actual name
            townBase = {
                "O": "Orlando",
                "J": "Jacksonville",
                "T": "Tampa",
                "TA": "Tallahassee",
                "M": "Miami",
                "S": "St. Petersburg",
                "C": "Cape Coral",
                "F": "Fort Lauderdale",
                "P": "Port St. Lucie"
            }

            if townCommand not in townBase:
                print("Hometown not found.")
                print(" ")
                time.sleep(2)
                continue
            
            chosenTown = townBase[townCommand]

            
            
            print(" ")
            print(f"Players from {chosenTown}:")
            print(" ")

            #Loop and print matches
            for row in rows:
                if len(row) < 4:
                    continue

                if row[3] == chosenTown:
                    print(row)
                    
            #Restart Prompt
            print(" ")
            retry = input("Search for another Hometown? (y/n) ")
            print("")
            
            if (retry == "n"):
                print("Good luck on getting onto the board!")
                break
            else:
                print("Going back to Hometown selection..")
                print(" ")
                time.sleep(2)
                continue
            
            
            
    #Rank Search        
    if (command == "r"):
        while True:
            rankCommand = input("Enter a number from 1-50: ")
            
            #Checks if what you fed the program is a number
            try:
                rankCommand = int(rankCommand)
            except ValueError:
                print("That's not an integer.")
                print(" ")
                continue
            else:
                print(" ")
            
            rankCommand = str(rankCommand)

            
            
            
            #For easier understanding of what prints
            print("[Username, Name, Rank, Hometown]")
            
            #Prints the player who has the rank
            for row in rows:
                if len(row) < 4:
                    continue

                if row[2] == rankCommand:
                    print(row)
                    
            
            #Restart Prompt
            print(" ")
            retry = input("Search for another Rank? (y/n) ")
            print("")
                    
            if (retry == "n"):
                print("Good luck on getting onto the board!")
                break
            else:
                print("Going back to Rank selection..")
                print(" ")
                time.sleep(2)
                continue
                
                
        
    #Display Entire Board
    if (command == "l"):
        while True:
            showLeaderboard(rows)
            
            #Restart Prompt
            print(" ")
            retry = input("Display Leaderboard Again? (y/n) ")
            print("")
                    
            if (retry == "n"):
                print("Good luck on getting onto the board!")
                break
            else:
                print("Going back to Rank selection..")
                print(" ")
                time.sleep(2)
                continue
        
main()
