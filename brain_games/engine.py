import prompt


def run_game(get_question_and_answer, description):

    SCORE_LIMIT = 3
    ROUNDS_NUMBER = 3
    score = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print(description)

    for _ in range(ROUNDS_NUMBER):
        question, correct_answer = get_question_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            score += 1
            print('Correct!')
            if score == SCORE_LIMIT:
                print('Congratulations,', name)
                break
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'"
            )
            break
