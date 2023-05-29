import prompt
import random


def is_even(num):
    """Returns True if num is even, False otherwise."""
    if num % 2 == 0:
        return True
    return False


def generate_secret_number():
    """Generates a random number between 1 and 20."""
    return random.randint(1, 20)


def main():
    score = 0
    round = 0

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    while round < 3:
        secret_number = generate_secret_number()
        round += 1
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', secret_number)
        answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if is_even(secret_number) else 'no'

        if answer == correct_answer:
            score += 1
            if score == 3:
                print('Correct!')
                print(f'Congratulations, {name}!')
                break
            else:
                print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.'", end="")
            print(f"Correct answer was '{correct_answer}.'")
            print(f"'Let's try again, {name}!")
            break


