import prompt


def start_game(correct_answer, rule):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(rule)

    count = 3
    while count > 0:
        question, answer = correct_answer()
        print(f'Question: {question}')
        ansver_player = prompt.string('Your answer: ')

        if ansver_player == answer:
            print('Correct!')
            count -= 1
        else:
            text = 'is wrong answer ;(. Correct answer was'
            print(f"'{ansver_player}' {text} '{answer}'.")
            print(f"Let's try again, {name}!")
            break

        if count == 0:
            print(f'Congratulations, {name}!')
