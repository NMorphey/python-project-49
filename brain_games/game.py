import prompt

from brain_games.cli import welcome_user


def play_a_game(game_rules: str, playsets: list):
    player_name = welcome_user()
    print(game_rules)
    for playset in playsets:
        question = playset[0]
        correct_answer = playset[1]
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')