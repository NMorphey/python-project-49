#!/usr/bin/env python3

from random import randint

import prompt

from brain_games.cli import welcome_user


def main():
    player_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    NUMBER_OF_ROUNDS = 3
    MIN_RANDOM_NUMBER = 1
    MAX_RANDOM_NUMBER = 40
    for i in range(NUMBER_OF_ROUNDS):
        question_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        print(f'Question: {question_number}')
        match (question_number % 2):
            case 0:
                correct_answer = 'yes'
            case 1:
                correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')


if __name__ == '__main__':
    main()