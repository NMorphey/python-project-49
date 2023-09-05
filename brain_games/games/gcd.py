#!/usr/bin/env python3

from random import randint


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(number_1, number_2):
    max_possible_divisor = min(number_1, number_2)
    for i in range(max_possible_divisor, 0, -1):
        if number_1 % i == 0 and number_2 % i == 0:
            return i


def get_playset():
    number_1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    correct_answer = get_gcd(number_1, number_2)
    question = f'{number_1} {number_2}'
    playset = (question, correct_answer)

    return playset
