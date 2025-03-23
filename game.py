import random
import os

def choose_difficulty():
    print("\nChoose Difficulty Level: ")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                return 10
            elif choice == 2:
                return 7
            elif choice == 3:
                return 5
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def load_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0
    return 0

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def number_guessing_game():

    score = 0
    high_score = load_high_score()

    print(f"\n🏆 Current High Score: {high_score} points")

    while True:
        print("\n🎯 Welcome to the Enhanced Number Guessing Game!")
        print("Think of a number between 1 and 100.")
        
        number_to_guess = random.randint(1, 100)
        max_attempts = choose_difficulty()
        attempts = 0

        while attempts < max_attempts:
            try:
                guess = int(input("Take a guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                    score += 10
                    break

                print(f"Attempts remaining: {max_attempts - attempts}")

            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if attempts >= max_attempts:
            print(f"❗ Game Over! The correct number was {number_to_guess}.")
            score -= 5

        print(f"Your current score is: {score}")

        # Update and Save High Score
        if score > high_score:
            print("🎊 New High Score! Congratulations!")
            high_score = score
            save_high_score(score)

        # Play Again Option
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'Y' and play_again != 'yes' and play_again != 'y':
            print(f"\nFinal Score: {score} points. Thanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    number_guessing_game()
