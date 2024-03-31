#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.constants import AP_DESCRIPTION, AP_SEQUENCE_LENGTH
import random


def generate_sequence():
    # generate first term
    first_term = random.randint(1, 100)

    # generate a common difference
    common_difference = random.randint(1, 10)

    # arithmetic sequence
    ap_sequence = []

    i = 0
    while i < AP_SEQUENCE_LENGTH:
        ap_sequence.append(first_term)
        first_term += common_difference
        i += 1

    return ap_sequence


def generate_round():

    sequence = generate_sequence()
    hidden_position = random.randint(0, AP_SEQUENCE_LENGTH)
    correct_answer = sequence[hidden_position]
    sequence[hidden_position] = '..'
    question = ''

    for element in sequence:
        question += str(element) + ' '

    return question, str(correct_answer)


def run_ap():
    run_game(generate_round, AP_DESCRIPTION)


if __name__ == '__main__':
    run_ap()
