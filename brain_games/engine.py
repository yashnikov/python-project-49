import prompt
from brain_games.constants import ROUNDS_NUMBER, SCORE_LIMIT


def run_game(generate_round, description):
    score = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}")
    print(description)

    for _ in range(ROUNDS_NUMBER):
        question, correct_answer = generate_round()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            score += 1
            print('Correct!')
            if score == SCORE_LIMIT:
                print(f"Congratulations, {name}!")
                break
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'"
            )
            print(f"Let's try again, {name}!")
            break
