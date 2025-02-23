from brain_games.game_logic import start_game
from brain_games.games.even_game import correct_answer

RULE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    start_game(correct_answer, RULE_GAME)


if __name__ == "__main__":
    main()
