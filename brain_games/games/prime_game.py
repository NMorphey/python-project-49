#!/usr/bin/env python3

from random import randint


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_brain_prime_playset():
    MIN_RANDOM_NUMBER = 1
    MAX_RANDOM_NUMBER = 100
    question = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    playset = (question, correct_answer)

    return playset
