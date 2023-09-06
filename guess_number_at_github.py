import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Set up the game loop
while True:
    # Ask the player to guess a number
    guess = int(input("Guess a number between 1 and 100: "))

    # Check if the guess is correct
    if guess == number:
        print("Congratulations, you guessed the number!")
        break

    # Give a hint about whether the guess is too high or too low
    if guess > number:
        print("Try a smaller number.")
    else:
        print("Try a larger number.")
        