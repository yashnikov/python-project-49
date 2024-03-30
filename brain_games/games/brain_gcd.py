#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.constants import GCD_DESCRIPTION
import random


def calculate_divisors(num):
    divisors = []

    i = 1
    while i <= num:
        if num % i == 0:
            divisors.append(i)
        i += 1

    return divisors


def find_gcd(n, m):
    n_divisors = calculate_divisors(n)
    m_divisors = calculate_divisors(m)
    gcd = max(set(n_divisors).intersection(m_divisors))
    return gcd


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    answer = find_gcd(num1, num2)
    question = f'{num1} {num2}'

    return question, str(answer)


def run_gcd():
    run_game(generate_round, GCD_DESCRIPTION)


if __name__ == '__main__':
    run_gcd()
