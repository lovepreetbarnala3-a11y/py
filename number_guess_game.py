import random


def play_game():
    initial_attempts = 8
    number = random.randint(1, 50)
    attempts_remaining = initial_attempts
    attempts_used = 0

    print(
        "Hi! Welcome to the Number Guessing Game!\n"
        "You have to guess a number between 1 and 50\n"
        f"and you only have {initial_attempts} attempts."
    )

    while attempts_remaining > 0:
        print(f"\nYou have {attempts_remaining} attempt{'s' if attempts_remaining > 1 else ''} remaining.")
        try:
            user_input = input("Guess a number (1-50): ")
            user_guess = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if not 1 <= user_guess <= 50:
            print("Please choose a number between 1 and 50.")
            continue

        attempts_used += 1

        if user_guess == number:
            print(
                f"Congrats! You got it right. You guessed the number {number} "
                f"in {attempts_used} attempt{'s' if attempts_used > 1 else ''}."
            )
            break
        elif user_guess < number:
            print("Your guess is too low. Try a higher number.")
        else:
            print("Your guess is too high. Try a lower number.")

        attempts_remaining -= 1
    else:
        # This runs only if the loop wasn't broken (i.e., player didn't guess it)
        print(f"\nGame over — you ran out of attempts. The number was {number}.")


if __name__ == "__main__":
    play_game()
