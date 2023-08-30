#!/usr/bin/env python3

from random import randint, choice

from brain_games.game import play_a_game


def main():
    game_rules = 'What is the result of the expression?'
    NUMBER_OF_ROUNDS = 3
    MIN_RANDOM_NUMBER = 1
    MAX_RANDOM_NUMBER = 40
    playsets = []
    for i in range(NUMBER_OF_ROUNDS):
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
        playsets.append(playset)

    play_a_game(game_rules, playsets)


if __name__ == '__main__':
    main()
