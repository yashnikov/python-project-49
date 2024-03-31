#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.constants import PRIME_DESCRIPTION
import random


def is_prime(number):
    if number == 1:
        return False
    if number == 2 or number == 3:
        return True

    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1

    return True


def generate_round():
    number = random.randint(1, 10)
    question = number
    answer = 'yes' if is_prime(number) else 'no'

    return question, answer


def run_prime():
    run_game(generate_round, PRIME_DESCRIPTION)


if __name__ == '__main__':
    run_prime()
