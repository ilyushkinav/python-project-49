from brain_games.game_logic import start_game
from brain_games.games.gcd_game import correct_answer

RULE_GAME = 'Find the greatest common divisor of given numbers.'


def main():
    start_game(correct_answer, RULE_GAME)


if __name__ == "__main__":
    main()