import random

x = random.randint(1, 100)

myString = int(input("Enter number to guess between 1 and 100: "))

while(myString != x):
    print("Wrong! Guess again!")
    myString = int(input("Enter number to guess: "))

print("Correct! The number is", x)


