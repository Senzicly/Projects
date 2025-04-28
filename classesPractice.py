import time
import keyboard

keyPress = keyboard.is_pressed

class player:
    
    def __init__(self, name: str, birthPlace: str, lvlBase: int):
        self.name = name
        self.birthPlace = birthPlace
        self.charLevel = 0.0
        self.lvlBase = 1.0
    
    def increaseLevel(self):
        self.charLevel += self.lvlBase
        
    def decreaseLevel(self):
        self.charLevel -= self.lvlBase
    
    def displayLevel(self):
        print(f"{self.name} of {self.birthPlace}!")
        print(f"you are level: {self.charLevel}")


def keyChecker(character):
    if (keyPress("z")):
        print("z was pressed.. level up!\n")
        character.increaseLevel()
        character.displayLevel()
        time.sleep(.05)
        
    elif (keyPress("x")):
        print("x was pressed.. lost a level..\n")
        character.decreaseLevel()
        character.displayLevel()
        time.sleep(.05)

    
def main():
    lvlBase = 1
    
    print("hey!! welcome to the game, lets get you started on creating your character. :3")
    name = input("what will your character's name be? be creative! ")
    time.sleep(.5)
    print(f"{name}? nice!! :]\n")
    birthPlace = input("where was your character born? it can be anywhere you want!! ")
    time.sleep(.5)
    print(f"i actually heard that {birthPlace} has pretty nice beaches, you should take me one day! >_<")
    print(f"okay {name} of {birthPlace}, the game begins now!\n")
    time.sleep(.5)
    
    character = player(name, birthPlace, lvlBase)
    
    print("press 'z' if you wish to level up and 'x' if you wish to lose a level!")
    print("if you want to stop the game, press 'a'!")

    while True:
        keyChecker(character)        
        
        if (character.charLevel > 100):
            character.lvlBase = 2
        
        if (character.charLevel > 250):
            character.lvlBase = 4
        
        if keyboard.is_pressed("a"):
            print("gone already?? alright then.. bye i guess, come back soon :(")
            break
        
        time.sleep(0.05)
        
main()
