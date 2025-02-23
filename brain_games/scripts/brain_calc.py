from brain_games.game_logic import start_game
from brain_games.games.calc_game import correct_answer

RULE_GAME = 'What is the result of the expression?'


def main():
    start_game(correct_answer, RULE_GAME)


if __name__ == "__main__":
    main()