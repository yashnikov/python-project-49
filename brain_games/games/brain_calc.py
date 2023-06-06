import prompt
import random
from brain_games.engine import generate_random_number, welcome_user


def play_calc():
    score = 0
    round = 0
    operators = ['+', '-', '*']

    name = welcome_user()
    print(f'Hello, {name}!')

    while round < 3:
        num1 = generate_random_number()
        num2 = generate_random_number()
        math_operation = random.choice(operators)
        correct_answer = ''

        round += 1
        print('What is the result of the expression?')
        answer = prompt.integer(f'Question: {num1} {math_operation} {num2} ')

        match math_operation:
            case '+':
                correct_answer = num1 + num2
            case '-':
                correct_answer = num1 - num2
            case '*':
                correct_answer = num1 * num2
        
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
            

