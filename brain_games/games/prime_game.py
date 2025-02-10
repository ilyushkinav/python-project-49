import prompt

from brain_games.game_logic import (
    congratulations,
    hello,
    name_player,
    num,
    start_game,
    wrong_answer,
)


def start_prime_game():
    start_game()
    name = name_player()
    print(hello(name))

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 3
    while count > 0:
        number = num()
        print(f'Question: {number}')
        ansver_player = prompt.string('Your answer: ')
        answer = 'yes'
        numbers_to_check = [2, 3, 5, 7]

        if number in numbers_to_check:
            answer = 'yes'
        elif number < 10:
            answer = 'no'
        else:
            for i in numbers_to_check:
                if number % i == 0:
                    answer = 'no'
                    break

        if ansver_player == answer:
            print('Correct!')
            count -= 1
        else:
            wrong_answer(ansver_player, answer, name)
            break
    if count == 0:
        print(congratulations(name))