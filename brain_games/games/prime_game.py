import random


def correct_answer():

    number = random.randint(1, 500)
    question = f'Question: {number}'
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

    return question, answer