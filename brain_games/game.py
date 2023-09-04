import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    player_name = prompt.string("May I have your name? ")
    print(f'Hello, {player_name}!')
    return player_name


NUMBER_OF_ROUNDS = 3


def play_a_game(game_module):
    player_name = welcome_user()
    print(game_module.DESCRIPTION)

    for _ in range(NUMBER_OF_ROUNDS):
        playset = game_module.get_playset()
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
