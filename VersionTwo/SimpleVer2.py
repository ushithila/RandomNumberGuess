import random

nums = input("Enter two numbers (seperated by commas): ")
x = nums.split(",")
rando = random.randint(int(x[0]), int(x[1]))
print(x[0])
myString = int(input("Guess a number between {} and {}: ".format(x[0], x[1])))

while(myString != rando):
    print("Wrong! Guess again.")
    myString = int(input("Guess a number between {} and {}: ".format(x[0], x[1])))
    

print("Correct! Number was ", rando)


