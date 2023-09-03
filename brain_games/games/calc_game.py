#!/usr/bin/env python3

from random import randint, choice


def get_brain_calc_playset():
    MIN_RANDOM_NUMBER = 1
    MAX_RANDOM_NUMBER = 40

    operand_1 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operand_2 = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operator = choice(['+', '-', '*'])
    match operator:
        case '+':
            correct_answer = operand_1 + operand_2
        case '-':
            correct_answer = operand_1 - operand_2
        case '*':
            correct_answer = operand_1 * operand_2
    question = f'{operand_1} {operator} {operand_2}'
    playset = (question, correct_answer)

    return playset
