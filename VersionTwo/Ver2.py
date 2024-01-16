import random

def rando():
    nums = input("Enter two numbers (seperated by commas): ")
    x = nums.split(",")
    rando = random.randint(int(x[0]), int(x[1]))
    myString = int(input("Guess a number between {} and {}: ".format(x[0], x[1])))

    while(myString != rando):
        print("Wrong! Guess again.")
        myString = int(input("Guess a number between {} and {}: ".format(x[0], x[1])))   

    print("Correct! Number was ", rando)

def main():
    rando()
    
if __name__ == '__main__':
    main()
