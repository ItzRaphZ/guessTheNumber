import random

min = 0
max = 20

random = random.randint(min, max)

settings = False

appIsRunning = True
gameIsRunning = False
Computer = False

print("Hello!")
print("Welcome to \"Guess The Number\", hope you have a wonderful day.\n")

while appIsRunning == True:
    if settings == False:
        print("[1] Guess the Number\n[2] Computer  Guesses the Number\n[3] Settings\n[0] Exit")
        option = int(input("Option: "))
    else:
        #SETTINGS
        print("settings")

    if option >= 0:
        if option <= 3:
            if option == 0:
                appIsRunning = False
                gameisRunning = False
            elif option == 1:
                appIsRunning = False
                gameisRunning = True
            elif option == 2:
                appIsRunning = False
                gameisRunning = True
            elif option == 3:
                settings = True
    else:
        print("\nERROR: Option not valid.")


while(gameIsRunning == True):
    guess = int(input("Insert a number: "))

    if(guess == random):
        gameIsRunning = False
    elif(guess > random):
        print("\n\nThe number is lower. Try again.")
    elif(guess < random):
        print("\n\nThe number is higher. Try again.")

print(f"\n\n\nCongratulations!! You guessed the number. The random number was: {random}\nBye bye")