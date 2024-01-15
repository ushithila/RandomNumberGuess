import random

def rando():
    x = random.randint(1, 100)

    myString = int(input("Enter number to guess between 1 and 100: "))

    while(myString != x):
        print("Wrong! Guess again!")
        myString = int(input("Enter number to guess: "))
    print("Correct! The number is", x)

def main():
    rando()
    choice = input("Play again?: ")
    while(choice.lower() == "yes"):
        rando()
        choice = input("Play again?: ")
        

if __name__ == '__main__':
    main()
