import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            # Get the user's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))

            # Validate the guess
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Increment the attempt counter
            attempts += 1

            # Check the user's guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")

guess_the_number()
