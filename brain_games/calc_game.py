import random
import prompt

from .game_logic import start_game, num, name_player, hello, wrong_answer, congratulations


def start_calc_game():
    start_game()
    name = name_player()
    print(hello(name))

    print('What is the result of the expression?')

    count = 3
    while count > 0:
        number_one = num()
        number_two = num()
        operation_sign = random.randint(1, 3)

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


        if ansver_player.isdigit() and int(ansver_player) == answer:
            print('Correct!')
            count -= 1
        else:
            wrong_answer(ansver_player, answer, name)
            break
    if count == 0:
        print(congratulations(name))