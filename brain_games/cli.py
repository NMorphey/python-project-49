import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    player_name = prompt.string("May I have your name? ")
    print(f'Hello, {player_name}!')