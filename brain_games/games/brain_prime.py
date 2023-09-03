#!/usr/bin/env python3

from random import randint

from brain_games.game import play_a_game


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    NUMBER_OF_ROUNDS = 3
    MIN_RANDOM_NUMBER = 1
    MAX_RANDOM_NUMBER = 100
    playsets = []
    for i in range(NUMBER_OF_ROUNDS):
        question = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        if is_prime(question):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        playset = (question, correct_answer)
        playsets.append(playset)

    play_a_game(game_rules, playsets)


if __name__ == '__main__':
    main()
