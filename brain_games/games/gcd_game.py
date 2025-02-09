import prompt

from brain_games.game_logic import (
    congratulations,
    hello,
    name_player,
    num,
    start_game,
    wrong_answer,
)


def start_gcd_game():
    start_game()
    name = name_player()
    print(hello(name))

    print('Find the greatest common divisor of given numbers.')

    count = 3

    while count > 0:
        number_one = num()
        number_two = num()
        min_number = min(number_one, number_two)
        max_number = max(number_one, number_two)
        print(f'Question: {number_one} {number_two}')

        answer = 0
        half_min = int(min_number / 2 + 1)

        if max_number % min_number == 0:
            answer = min_number
        else:
            for i in range(half_min, 0, -1):
                if max_number % i == 0 and min_number % i == 0:
                    answer = i
                    break

        ansver_player = prompt.string('Your answer: ')

        if ansver_player.isdigit() and int(ansver_player) == answer:
            print('Correct!')
            count -= 1
        else:
            wrong_answer(ansver_player, answer, name)
            break
    if count == 0:
        print(congratulations(name))