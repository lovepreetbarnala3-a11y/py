import random

print("Hi! Welcome to the Number Guessing Game!,\nYou have to guess a number between 1 and 50\nand you only have 8 attempts")
number = random.randint(1, 50)
attempts = 8
guess = 0
while guess <8:
    print(f"you have {attempts} attempts remaining.")
    user_guess = int(input("Guess a number: "))
    if user_guess == number:
        print(f"congrats,You got it right!. you guessed the {number} number in {attempts} attempts. ")
        break
    else :
        if user_guess < number:
            higher_or_lower = 'higher'

        else :
            higher_or_lower = 'lower'

        print(f"Your guess is wrong. Try {higher_or_lower} number.")
    guess += 1
    attempts -= 1

print(f"Your number was {number} game over!!")