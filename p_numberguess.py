import random

rangelimit = int(input("Type the range limit of guessing a number: "))

if rangelimit <= 0:
    print("Please enter a number greater than 0.")
    quit()

guesscount = 0
randomnum = random.randint(0, rangelimit)
while True:
    user_guess = int(input("Make a guess: "))
    guesscount += 1
    if user_guess == randomnum:
        print("You got it!!!!")
        break
    else:
        print("Wrong guess!!! Try again dear!")

print("You have guessed it right in", guesscount, "guesses. Well done!!!")
    
