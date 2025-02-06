import prompt

from .game_logic import start_game, num, name_player, hello, wrong_answer, congratulations


def start_even_game():
    start_game()
    name = name_player()
    print(hello(name))

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 3
    while count > 0:
        number = num()
        print(f'Question: {number}')
        ansver_player = prompt.string('Your answer: ')
        answer = ''
        if number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

        if ansver_player == answer:
            print('Correct!')
            count -= 1
        else:
            wrong_answer(ansver_player, answer, name)
            break
    if count == 0:
        print(congratulations(name))