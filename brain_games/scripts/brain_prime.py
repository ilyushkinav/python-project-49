from brain_games.game_logic import start_game
from brain_games.games.prime_game import correct_answer

RULE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    start_game(correct_answer, RULE_GAME)


if __name__ == "__main__":
    main()