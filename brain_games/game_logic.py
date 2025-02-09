import random

import prompt


def start_game():
    print("Welcome to the Brain Games!")


def name_player():
    name_input = prompt.string('May I have your name? ')
    return name_input


def hello(name):
    return f'Hello, {name}!'


def wrong_answer(ansver_player, answer, name):
    text = 'is wrong answer ;(. Correct answer was'
    print(f"'{ansver_player}' {text} '{answer}'.")
    print(f"Let's try again, {name}!")


def congratulations(name):
    return f'Congratulations, {name}!'


def num(num_one=1, num_two=100):
    num = random.randint(num_one, num_two)
    return num