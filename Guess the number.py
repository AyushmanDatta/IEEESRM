import random

# Set the range of the random number to guess
MIN_RANGE = 1
MAX_RANGE = 100

# Generate a random number to guess
number_to_guess = random.randint(MIN_RANGE, MAX_RANGE)

# Initialize the number of guesses
num_guesses = 0

# Loop until the user guesses the correct number
while True:
    # Ask the user to guess a number
    guess = int(input(f"Guess a number between {MIN_RANGE} and {MAX_RANGE}: "))
    num_guesses += 1

    # Check if the guess is correct
    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
        break
    elif guess < number_to_guess:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
