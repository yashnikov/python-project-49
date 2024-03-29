import prompt


def run_game(get_question_and_answer, description):
    score = 0
    rounds_number = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print(description)

    for _ in range(rounds_number):
        question, correct_answer = get_question_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            score += 1
            print('Correct!')
            if score == 3:
                print('Congratulations,', name)
                break
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'"
            )
            break
