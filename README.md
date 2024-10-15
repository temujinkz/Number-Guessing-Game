# Explanation:
Imports:
<p>
random: Used to generate a random number within the specified range.
Main Game Logic:
<p>
Game Setup: The user first inputs the range (lower and upper bounds) for the number they need to guess.
Random Number Generation: The script generates a random number using random.randint(lower_bound, upper_bound).<p>
  
# Game Loop:
<p>
The player is prompted to guess the number.
If the guess is too low or too high, a hint is given.
The loop continues until the user guesses the correct number.
The total number of attempts is tracked and displayed when the correct number is guessed.
  
# Usage Example:

<code>
Welcome to the Number Guessing Game!
Enter the lower bound of the range: 1
Enter the upper bound of the range: 100
Guess the number between 1 and 100!
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Congratulations! You've guessed the number 37 in 3 attempts.
</code>

# Modifications:
<p>
You can modify the game to set a fixed number of attempts, or provide an option to play again after a correct guess.
