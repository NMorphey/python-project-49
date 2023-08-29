import prompt


def welcome_user():
    """"Shows welcome message and receives player's name, then returns it."""
    print('Welcome to the Brain Games!')
    player_name = prompt.string("May I have your name? ")
    print(f'Hello, {player_name}!')
    return player_name
