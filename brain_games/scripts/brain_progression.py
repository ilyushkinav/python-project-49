from brain_games.game_logic import start_game
from brain_games.games.progression_game import correct_answer

RULE_GAME = 'What number is missing in the progression?'


def main():
    start_game(correct_answer, RULE_GAME)


if __name__ == "__main__":
    main()