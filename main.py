import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the number
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Generate a random number within the given range
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    print(f"Guess the number between {lower_bound} and {upper_bound}!")
    
    while True:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check if the guess is correct
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
