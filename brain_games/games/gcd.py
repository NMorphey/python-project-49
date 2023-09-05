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
    random_number_1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    random_number_2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    correct_answer = get_gcd(random_number_1, random_number_2)
    question = f'{random_number_1} {random_number_2}'
    playset = (question, correct_answer)

    return playset
