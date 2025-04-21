#luis d
#im attempting to rekindle the flame of programming, in three minutes.
#April 20th, 2025; 04/20/2025
#make a program that lets you input your name, DOB, todays date, and your grade level.
#then without the timer, improve upon it, make it yours.

def main():
    name = input("hey, my name is dataBot, what is yours? ").lower()

    if ("l" in name):
        print(f"is that you.. {name}? ")
        name = name + "."
    else:
        print("mm")

    dob = input("what a nice name.. what year were you born? ")
    sympathy = input("interesting, i don't know when i was born, what do you have to say about that? ")

    if ("sorry" in sympathy):
        print("it's fine, thank you.")
    else:
        print("hmm")

    date = input("sorry for bothering you so much, but what's the year right now? ")
    print("wow.. im sorry, it's just been so long.. ")
    print(" ")
    print("thank you, now ill spit all of this back at you, like i was programmed to do. ")
    print(" ")
    print(f"hey {name}. today is {date} (damn..), you were born on {dob}, and you responded, {sympathy}, to my reaction. ")

main()
