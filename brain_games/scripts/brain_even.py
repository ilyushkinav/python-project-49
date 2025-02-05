import random
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 3
    while count > 0:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        ansver_player = prompt.string('Your answer: ')
        right_answer = ''
        if num % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'


        if ansver_player == right_answer:
            print('Correct!')
            count -= 1
        else:
            print(f"'{ansver_player}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 0:
        print(f'Congratulations, {name}!')
