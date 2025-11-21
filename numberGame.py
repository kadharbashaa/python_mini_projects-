import random

print("🎮 Welcome to Number Guessing Game!")

# computer chooses a number
number = random.randint(1, 20)

while True:
    try:
        guess = int(input("Guess a number between 1 and 20: "))

        if guess < number:
            print("Too low! Try again.\n")

        elif guess > number:
            print("Too high! Try again.\n")

        else:
            print("🎉 Correct! You guessed the number!")
            break

    except ValueError as e:
        print("Oops! Please enter a valid number.\n")
