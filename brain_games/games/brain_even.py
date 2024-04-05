#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.constants import EVEN_DESCRIPTION
import random


def generate_round():
    random_integer = random.randint(1, 40)
    answer = 'yes' if random_integer % 2 == 0 else 'no'
    return random_integer, answer


def run_even():
    run_game(generate_round, EVEN_DESCRIPTION)


if __name__ == '__main__':
    run_even()
