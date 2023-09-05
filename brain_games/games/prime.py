from random import randint


MIN_RANDOM_NUMBER = -5
MAX_RANDOM_NUMBER = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_playset():
    random_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    playset = (random_number, correct_answer)

    return playset
