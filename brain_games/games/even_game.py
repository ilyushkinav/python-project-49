import random


def correct_answer_even():

    number = random.randint(1, 100)

    answer = ''
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return number, answer