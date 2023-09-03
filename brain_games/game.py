import prompt

from brain_games.cli import welcome_user
from brain_games.games.calc_game import get_brain_calc_playset
from brain_games.games.even_game import get_brain_even_playset
from brain_games.games.gcd_game import get_brain_gcd_playset
from brain_games.games.prime_game import get_brain_prime_playset
from brain_games.games.progression_game import get_brain_progression_playset


NUMBER_OF_ROUNDS = 3
game_rules = {
    'calc': 'What is the result of the expression?',
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'gcd': 'Find the greatest common divisor of given numbers.',
    'prime': 'Answer "yes" if given number is prime. Otherwise answer "no".',
    'progression': 'What number is missing in the progression?'
}


def play_a_game(game_type: str):
    player_name = welcome_user()
    print(game_rules[game_type])

    for _ in range(NUMBER_OF_ROUNDS):
        playset = get_playset(game_type)
        question = playset[0]
        correct_answer = str(playset[1])
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            wrong_answer_text = 'is wrong answer ;(. Correct answer was'
            print(f"'{answer}' {wrong_answer_text} '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')


def get_playset(game_type):
    match game_type:
        case 'calc':
            return get_brain_calc_playset()
        case 'even':
            return get_brain_even_playset()
        case 'gcd':
            return get_brain_gcd_playset()
        case 'prime':
            return get_brain_prime_playset()
        case 'progression':
            return get_brain_progression_playset()
