from random import randint


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 40
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_playset():
    question_number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if question_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    playset = (question_number, correct_answer)

    return playset
