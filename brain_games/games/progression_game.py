import random


def correct_answer_progression():

    count_number = random.randint(5, 10)
    start_number = random.randint(1, 40)
    step = random.randint(2, 5)
    progression_numbers = [str(start_number)]
    result_number = start_number

    for i in range(count_number):
        result_number += step
        progression_numbers.append(str(result_number))

    question_number = random.randint(0, len(progression_numbers) - 1)
    answer = progression_numbers[question_number]
    progression_numbers[question_number] = '..'

    question = f'Question: {' '.join(progression_numbers)}'

    return question, answer