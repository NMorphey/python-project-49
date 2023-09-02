#!/usr/bin/env python3

from random import randint

from brain_games.game import play_a_game


def main():
    game_rules = 'Find the greatest common divisor of given numbers.'
    NUMBER_OF_ROUNDS = 3
    MIN_RANDOM_NUMBER = 1
    MAX_RANDOM_NUMBER = 100
    playsets = []
    for i in range(NUMBER_OF_ROUNDS):
        number_1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        number_2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        max_possible_divisor = min(number_1, number_2)
        correct_answer = 1
        for i in range(max_possible_divisor, 1, -1):
            if number_1 % i == 0 and number_2 % i == 0:
                correct_answer = i
        question = f'{number_1} {number_2}'
        playset = (question, correct_answer)
        playsets.append(playset)

    play_a_game(game_rules, playsets)


if __name__ == '__main__':
    main()
