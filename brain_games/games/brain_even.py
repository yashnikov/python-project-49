#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random


def is_even(number):
    return number % 2 == 0


def play_even():
    name = welcome_user()

    round = 0
    score = 0

    while round < 3:
        random_integer = random.randint(1, 20)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', random_integer)

        # correct answer
        correct_answer = ''
        if is_even(random_integer):
            correct_answer = "yes"
        else:
            correct_answer = "no"

        user_choice = input()

        if user_choice == correct_answer:
            score += 1
            print('Correct!')
        else:
            print(
                f"'{user_choice}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'"
            )
            break

        if score == 3:
            print('Congratulations,', name)
            break


def main():
    name = welcome_user()
    play_even()


if __name__ == '__main__':
    main()
