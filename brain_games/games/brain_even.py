#!/usr/bin/env python3
from brain_games.engine import run_game
import random

EVEN_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    random_integer = random.randint(1, 40)
    answer = 'yes' if is_even(random_integer) else 'no'
    return random_integer, answer


def run_even():
    run_game(get_question_and_answer, EVEN_DESCRIPTION)


if __name__ == '__main__':
    run_even()
