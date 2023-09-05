from random import randint

import math


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_playset():
    random_number_1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number_2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    correct_answer = math.gcd(random_number_1, random_number_2)
    question = f'{random_number_1} {random_number_2}'
    playset = (question, correct_answer)

    return playset
