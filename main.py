import random

min = 0
max = 20

random = random.randint(min, max)

gameIsRunning = True

print("Hello!")
print("Welcome to \"Guess The Number\", hope you have a wonderful day.\n")

while(gameIsRunning == True):
    guess = int(input("Insert a number: "))

    if(guess == random):
        gameIsRunning = False
    elif(guess > random):
        print("\n\nThe number is lower. Try again.")
    elif(guess < random):
        print("\n\nThe number is higher. Try again.")

print(f"\n\n\nCongratulations!! You guessed the number. The random number was: {random}\nBye bye")