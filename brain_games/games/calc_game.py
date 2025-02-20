import prompt

from brain_games.game_logic import (
    congratulations,
    hello,
    name_player,
    num,
    start_game,
    wrong_answer,
)


def start_calc_game():
    start_game()
    name = name_player()
    print(hello(name))

    print('What is the result of the expression?')

    count = 3
    while count > 0:
        number_one = num()
        number_two = num()
        operation_sign = num(1, 3)

        answer = 0

        if operation_sign == 1:
            print(f'Question: {number_one} + {number_two}')
            answer = number_one + number_two
        elif operation_sign == 2:
            print(f'Question: {number_one} - {number_two}')
            answer = number_one - number_two
        elif operation_sign == 3:
            print(f'Question: {number_one} * {number_two}')
            answer = number_one * number_two

        ansver_player = prompt.string('Your answer: ')
        convert_answer_player = ''
        if ansver_player[0] == '-':
            convert_answer_player = ansver_player[1:]
            ansver_player = convert_answer_player

            if ansver_player.isdigit() and int(ansver_player) == answer * (-1):
                print('Correct!')
                count -= 1
            else:
                wrong_answer(ansver_player, answer, name)
                print('Hyeta2')
                break

        elif ansver_player.isdigit() and int(ansver_player) == answer:
            print('Correct!')
            count -= 1
        else:
            wrong_answer(ansver_player, answer, name)
            break
    if count == 0:
        print(congratulations(name))