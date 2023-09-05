#!/usr/bin/env python3

from random import randint


MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 30
MIN_PROGRESSION_LEN = 5
MAX_PROGRESSION_LEN = 10
MIN_COMMON_DIFFERENCE = 2
MAX_COMMON_DIFFERENCE = 9
DESCRIPTION = 'What number is missing in the progression?'


def get_playset():
    first_number = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    progression_len = randint(MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN)
    common_difference = randint(MIN_COMMON_DIFFERENCE, MAX_COMMON_DIFFERENCE)
    progression = range(first_number,
                        first_number + progression_len * common_difference + 1,
                        common_difference)
    progression = list(map(str, progression))
    excluded_number_index = randint(0, progression_len - 1)
    excluded_number = progression[excluded_number_index]
    progression[excluded_number_index] = '..'
    question = ' '.join(progression)
    playset = (question, excluded_number)

    return playset
