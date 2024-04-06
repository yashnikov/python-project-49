#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.constants import PRIME_DESC
import random


def is_prime(number: int) -> bool:
    if number == 1:
        return False
    if number in (2, 3):
        return True

    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1

    return True


def generate_round() -> tuple[str, str]:
    number = random.randint(1, 10)
    question = number
    answer = 'yes' if is_prime(number) else 'no'

    return question, answer


def run_prime() -> None:
    run_game(generate_round, PRIME_DESC)


if __name__ == '__main__':
    run_prime()
