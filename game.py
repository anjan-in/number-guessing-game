import random
import os
import time
import pygame
from colorama import Fore, Style, init

# Initialize Colorama for Windows
init(autoreset = True)

# Initialize Pygame for Sound Effects
pygame.mixer.init()

def play_sound(sound_file):
    try:
        pygame.mixer.Sound(f"sounds/{sound_file}").play()
    except Exception as e:
        print(Fore.RED + f"Error playing sound: {e}")

def choose_difficulty():
    print("\nChoose Difficulty Level: ")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    
    while True:
        try:
            choice = int(input(Fore.CYAN + "Enter your choice (1/2/3): "))
            if choice == 1:
                return 10
            elif choice == 2:
                return 7
            elif choice == 3:
                return 5
            else:
                print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

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

def get_custom_range():
    while True:
        try:
            min_num = int(input(Fore.MAGENTA + "Enter the minimum number for the range: "))
            max_num = int(input(Fore.MAGENTA + "Enter the maximum number for the range: "))
            if min_num >= max_num:
                print(Fore.RED + "Invalid range. Minimum must be less than Maximum.")
            else:
                return min_num, max_num
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")

def number_guessing_game():

    score = 0
    high_score = load_high_score()

    print(Fore.YELLOW + f"\n🏆 Current High Score: {high_score} points")

    while True:
        print(Fore.CYAN + "\n🎯 Welcome to the Number Guessing Game!")
        # print("Think of a number between 1 and 100.")

        min_num, max_num = get_custom_range()
        print(Fore.CYAN + f"I've chosen a number between {min_num} and {max_num}. Try to guess it!")
        
        number_to_guess = random.randint(min_num, max_num)
        max_attempts = choose_difficulty()
        attempts = 0

        # Start Timer
        start_time = time.time()

        while attempts < max_attempts:
            try:
                guess = int(input("Take a guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print(Fore.YELLOW + "Too low! Try again.")
                elif guess > number_to_guess:
                    print(Fore.YELLOW + "Too high! Try again.")
                else:
                    end_time = time.time()
                    elapsed_time = round(end_time - start_time, 2)
                    print(Fore.GREEN + f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                    print(Fore.GREEN + f"⏱ Time Taken: {elapsed_time} seconds.")
                    play_sound("win.wav")
                    score += 10
                    break

                print(Fore.CYAN + f"Attempts remaining: {max_attempts - attempts}")

            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
        
        if attempts >= max_attempts:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(Fore.RED + f"❗ Game Over! The correct number was {number_to_guess}.")
            print(Fore.RED + f"⏱ Time Taken: {elapsed_time} seconds.")
            play_sound("lose.wav")
            score -= 5

        print(Fore.YELLOW + f"Your current score is: {score}")

        # Update and Save High Score
        if score > high_score:
            print(Fore.GREEN + "🎊 New High Score! Congratulations!")
            high_score = score
            play_sound("highscore.wav")
            save_high_score(score)

        # Play Again Option
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'Y' and play_again != 'yes' and play_again != 'y':
            print(Fore.YELLOW + f"\nFinal Score: {score} points. Thanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    number_guessing_game()


def generate_number(min_num, max_num):
    return random.randint(min_num, max_num)

def check_guess(user_guess, actual_number):
    if user_guess < actual_number:
        return "too low"
    elif user_guess > actual_number:
        return "too high"
    else:
        return "correct"