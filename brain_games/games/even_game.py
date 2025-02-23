import random


def correct_answer():

    number = random.randint(1, 100)

    answer = ''
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return number, answer