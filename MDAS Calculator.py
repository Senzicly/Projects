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
    return a / b

def main():
    print("HELLO, I AM YOUR CALCULATOR BOT, HERE TO ASSIST YOU WITH YOUR CALCULATIONS.")

    oper = input("WILL YOU ADD, SUBTRACT, MULTIPLY, OR DIVIDE? ")

    print("IF YOU'RE SUBTRACTING, THE SECOND NUMBER YOU INPUT WILL BE TAKEN OUT FROM THE FIRST NUMBER.")
    print("IF YOU'RE DIVIDING, THE SECOND NUMBER YOU INPUT WILL BE WHAT THE FIRST NUMBER IS DIVDED BY.")

    a = int(input("WHAT IS YOUR FIRST NUMBER? "))
    b = int(input("WHAT IS YOUR SECOND NUMBER? "))
    
    
    if (oper == "add"):
        ans = ADD(a,b)
    
    if (oper == "subtract"):
        ans = SUBTRACT(a,b)
    
    if (oper == "multiply"):
        ans = MULTIPLY(a,b)
    
    if (oper == "divide"):
        ans = DIVIDE(a,b)
    print("YOUR ANSWER IS " + str(ans))
main()