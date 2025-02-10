import random

import prompt


# We display the welcome window.
def start_game():
    print("Welcome to the Brain Games!")


# We find out the player's name and write it into a variable.
def name_player():
    name_input = prompt.string('May I have your name? ')
    return name_input


# We greet the player by name.
def hello(name):
    return f'Hello, {name}!'


# We return a message to the player that the answer is incorrect.
def wrong_answer(ansver_player, answer, name):
    text = 'is wrong answer ;(. Correct answer was'
    print(f"'{ansver_player}' {text} '{answer}'.")
    print(f"Let's try again, {name}!")


# Congratulations to the player on his victory.
def congratulations(name):
    return f'Congratulations, {name}!'


# Returns a random number.
def num(num_one=1, num_two=100):
    num = random.randint(num_one, num_two)
    return num