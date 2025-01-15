import random

correct_guess = 0
wrong_guess = 0


while True:
    fingers = random.randint(1,5)
    give_up = input("\n\nPress Q to give up or press any other key to play. ").lower()
    if give_up == 'q':
        break
    else:
        guess = input("How many fingers am I holding up? Enter a number between 1 and 5:")

    try:
        guess = int(guess)
        if guess == fingers:
            correct_guess += 1
            print(f"\nCorrect! You've guessed {fingers} fingers correctly.")
        else:
            wrong_guess += 1
            print(f"\nI was holding up {fingers} fingers.")

        if correct_guess + wrong_guess > 0:
            win_percentage = round(correct_guess / (correct_guess + wrong_guess) * 100, 6)
            win_percentage = f"{win_percentage}%"
        else:
            win_percentage = "0%"

        print(f"Correct guesses: {correct_guess}, Wrong guesses: {wrong_guess}. That's a win percentage of {win_percentage}.")


    except ValueError:
        print("That's not a valid number. Please enter a digit between 1 and 5.")


print(f"Thanks for playing! Your final win percentage was: {win_percentage}")










