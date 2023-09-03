#!/usr/bin/env python3

from random import randint


def get_brain_even_playset():
    MIN_RANDOM_NUMBER = 1
    MAX_RANDOM_NUMBER = 40
    question_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    match (question_number % 2):
        case 0:
            correct_answer = 'yes'
        case 1:
            correct_answer = 'no'
    playset = (question_number, correct_answer)

    return playset
