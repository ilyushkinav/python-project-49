import random


def correct_answer_gcd():

    number_one = random.randint(1, 50)
    number_two = random.randint(1, 50)
    min_number = min(number_one, number_two)
    max_number = max(number_one, number_two)

    question = f'Question: {number_one} {number_two}'
    answer = ''
    half_min = int(min_number / 2 + 1)

    if max_number % min_number == 0:
        answer = str(min_number)
    else:
        for i in range(half_min, 0, -1):
            if max_number % i == 0 and min_number % i == 0:
                answer = str(i)
                break

    return question, answer