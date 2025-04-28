import time
import keyboard

keyPress = keyboard.is_pressed

class player:
    
    def __init__(self, name: str, birthPlace: str):
        self.name = name
        self.birthPlace = birthPlace
        self.charLevel = 0
    
    def increaseLevel(self):
        self.charLevel += 1
        
    def decreaseLevel(self):
        self.charLevel -= 1
    
    def displayLevel(self):
        print(f"{self.name} of {self.birthPlace}!")
        print(f"you are level: {self.charLevel}")


def keyChecker(character):
    if (keyPress("z")):
        print("z was pressed.. level up!")
        character.increaseLevel()
        character.displayLevel()
        time.sleep(.5)
        
    elif (keyPress("x")):
        print("x was pressed.. lost a level..")
        character.decreaseLevel()
        character.displayLevel()
        time.sleep(.5)

    
def main():
    print("hey!! welcome to the game, lets get you started on creating your character. :3")
    name = input("what will your character's name be? be creative! ")
    time.sleep(.5)
    print(f"{name}? nice!! :]")
    birthPlace = input("where was your character born? it can be anywhere you want!! ")
    time.sleep(.5)
    print(f"i actually heard that {birthPlace} has pretty nice beaches, you should take me one day! >_<")
    print(f"okay {name} of {birthPlace}, the game begins now!")
    time.sleep(.5)
    
    character = player(name, birthPlace)
    
    print("press 'z' if you wish to level up and 'x' if you wish to lose a level!")
    print("if you want to stop the game, press 'a'!")

    while True:
        keyChecker(character)        
        
        if keyboard.is_pressed("a"):
            print("gone already?? alright then.. bye i guess, come back soon :(")
            break
        
        time.sleep(0.05)
        
main()
