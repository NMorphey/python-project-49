import prompt


NUMBER_OF_ROUNDS = 3


def play(game):
    print('Welcome to the Brain Games!')
    player_name = prompt.string("May I have your name? ")
    print(f'Hello, {player_name}!')
    print(game.DESCRIPTION)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_playset()
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
