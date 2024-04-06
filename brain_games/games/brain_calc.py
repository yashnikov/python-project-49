#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.constants import CALC_DESCRIPTION
import random


def generate_round() -> tuple[str, str]:
    operators = ['+', '-', '*']

    num1: int = random.randint(1, 10)
    num2: int = random.randint(1, 10)
    math_operation = random.choice(operators)
    correct_answer = ''

    match math_operation:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2

    question = f'{num1} {math_operation} {num2}'

    return question, str(correct_answer)


def run_calc() -> None:
    run_game(generate_round, CALC_DESCRIPTION)


if __name__ == '__main__':
    run_calc()
