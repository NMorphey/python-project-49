#!/usr/bin/env python3

from random import randint

import prompt

from brain_games.game import play_a_game


def main():
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    NUMBER_OF_ROUNDS = 3
    MIN_RANDOM_NUMBER = 1
    MAX_RANDOM_NUMBER = 40
    playsets = []
    for i in range(NUMBER_OF_ROUNDS):
        question_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        match (question_number % 2):
            case 0:
                correct_answer = 'yes'
            case 1:
                correct_answer = 'no'
        playset = (question_number, correct_answer)
        playsets.append(playset)
    
    play_a_game(game_rules, playsets)
    
        
if __name__ == '__main__':
    main()