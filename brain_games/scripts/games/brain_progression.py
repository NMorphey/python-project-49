#!/usr/bin/env python3

from random import randint

from brain_games.game import play_a_game


def main():
    game_rules = 'What number is missing in the progression?'
    NUMBER_OF_ROUNDS = 3
    MIN_FIRST_NUMBER = 1
    MAX_FIRST_NUMBER = 30
    MIN_PROGRESSION_LEN = 5
    MAX_PROGRESSION_LEN = 10
    MIN_STEP = 2
    MAX_STEP = 9
    playsets = []
    for i in range(NUMBER_OF_ROUNDS):
        first_number = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
        progression_len = randint(MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN)
        step = randint(MIN_STEP, MAX_STEP)
        progression = range(first_number,
                            first_number + progression_len*step + 1,
                            step)
        progression = list(map(str, progression))
        excluded_number_index = randint(1, progression_len - 2)
        excluded_number = progression[excluded_number_index]
        progression[excluded_number_index] = '..'
        question = ' '.join(progression)
        playset = (question, excluded_number)
        playsets.append(playset)

    play_a_game(game_rules, playsets)


if __name__ == '__main__':
    main()
