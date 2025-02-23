import random


def correct_answer_calc():

    number_one = random.randint(1, 10)
    number_two = random.randint(1, 10)
    operation_sign = random.randint(1, 3)
    question = ''
    answer = 0

    if operation_sign == 1:
        question = f'Question: {number_one} + {number_two}'
        answer = str(number_one + number_two)
    elif operation_sign == 2:
        question = f'Question: {number_one} - {number_two}'
        answer = str(number_one - number_two)
    elif operation_sign == 3:
        question = f'Question: {number_one} * {number_two}'
        answer = str(number_one * number_two)

    return question, answer