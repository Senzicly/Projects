#Luis
#Start Date : 11/20/24, End Date: 11/20/24
#MDAS (Multiply, Divide, Add, Subtract) Calculator

def ADD(a, b):
    return a + b

def SUBTRACT(a, b):
    return a - b

def MULTIPLY(a, b):
    return a * b

def DIVIDE(a, b):
    if (b == 0):
        return "-ERROR DETECTED! DO NOT ENTER 0, YOU CANNOT DIVIDE BY 0"
    return a / b

def main():

    print("HELLO, I AM YOUR CALCULATOR BOT, HERE TO ASSIST YOU WITH YOUR CALCULATIONS.")
    
    
    while True:
        print('TYPE "QUIT" WHEN ASKED TO ENTER AN OPERATOR TO STOP THE CALCULATOR')
        oper = input("WILL YOU ADD, SUBTRACT, MULTIPLY, OR DIVIDE? ").lower()
        
        if (oper == "quit"):
            print('OPTION "QUIT" SELECTED, I HOPE I HAVE ASSISTED YOU!')
            break 
        if oper not in ("add", "subtract", "multiply", "divide", " "):
            print('PLEASE ENTER "ADD", "SUBTRACT", "MULTIPLY", OR "DIVIDE".')
            continue
        
        print(" ")
        
        print("IF YOU'RE SUBTRACTING, THE SECOND NUMBER YOU INPUT WILL BE TAKEN OUT FROM THE FIRST NUMBER.")
        print("IF YOU'RE DIVIDING, THE SECOND NUMBER YOU INPUT WILL BE WHAT THE FIRST NUMBER IS DIVDED BY.")

        try:
            a = float(input("WHAT IS YOUR FIRST NUMBER? "))
        except ValueError:
            print("PLEASE ENTER A NUMBER, NOTHING ELSE.")
            continue

        try:
            b = float(input("WHAT IS YOUR SECOND NUMBER? "))
        except ValueError:
            print("PLEASE ENTER A NUMBER, NOTHING ELSE.")
            continue
        
        if (oper == "add"):
            ans = ADD(a,b)
        
        elif (oper == "subtract"):
            ans = SUBTRACT(a,b)
        
        elif (oper == "multiply"):
            ans = MULTIPLY(a,b)
        
        elif (oper == "divide"):
            ans = DIVIDE(a,b)
            
        print(f"YOUR ANSWER IS {ans}")

main()

