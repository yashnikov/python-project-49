import random
import prompt

def generate_random_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 10)


def welcome_user():
    name = prompt.string('May I have your name? ')
    return name

