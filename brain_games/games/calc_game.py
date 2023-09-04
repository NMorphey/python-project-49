#!/usr/bin/env python3

from random import randint, choice


MIN_RANDOM_NUMBER = -40
MAX_RANDOM_NUMBER = 40
DESCRIPTION = 'What is the result of the expression?'

def get_playset():
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
