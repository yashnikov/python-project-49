#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.constants import AP_DESCRIPTION, AP_SEQUENCE_LENGTH
import random


def generate_sequence() -> list[int]:
    # generate first term
    first_term = random.randint(1, 100)

    # generate a common difference
    common_difference = random.randint(1, 10)

    # arithmetic sequence
    ap_sequence = []

    ap_sequence = [
        first_term + common_difference * i for i in range(AP_SEQUENCE_LENGTH)
    ]

    return ap_sequence


def generate_round() -> tuple[str, str]:

    sequence = generate_sequence()
    hidden_position = random.randint(0, AP_SEQUENCE_LENGTH - 1)
    correct_answer = sequence[hidden_position]
    sequence[hidden_position] = '..'
    question = ' '.join(map(str, sequence))

    return question, str(correct_answer)


def run_ap() -> None:
    run_game(generate_round, AP_DESCRIPTION)


if __name__ == '__main__':
    run_ap()
