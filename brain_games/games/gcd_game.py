#!/usr/bin/env python3

from random import randint


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_brain_gcd_playset():
    number_1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    max_possible_divisor = min(number_1, number_2)
    correct_answer = 1
    for i in range(max_possible_divisor, 1, -1):
        if number_1 % i == 0 and number_2 % i == 0:
            correct_answer = i
            break
    question = f'{number_1} {number_2}'
    playset = (question, correct_answer)

    return playset
