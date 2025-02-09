import prompt

from brain_games.game_logic import (
    congratulations,
    hello,
    name_player,
    num,
    start_game,
    wrong_answer,
)


def start_progression_game():
    start_game()
    name = name_player()
    print(hello(name))

    print('What number is missing in the progression?')

    count = 3

    while count > 0:
        count_number = num(5, 10)
        start_number = num(1, 40)
        step = num(2, 5)
        progression_numbers = [str(start_number)]
        result_number = start_number

        for i in range(count_number):
            result_number += step
            progression_numbers.append(str(result_number))

        question_number = num(0, len(progression_numbers) - 1)
        answer = int(progression_numbers[question_number])
        progression_numbers[question_number] = '..'

        print(f'Question: {' '.join(progression_numbers)}')

        ansver_player = prompt.string('Your answer: ')

        if ansver_player.isdigit() and int(ansver_player) == answer:
            print('Correct!')
            count -= 1
        else:
            wrong_answer(ansver_player, answer, name)
            break

    if count == 0:
        print(congratulations(name))