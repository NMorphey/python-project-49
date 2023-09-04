#!/usr/bin/env python3

from brain_games.game import play_a_game
from brain_games.games import calc_game


def main():
    play_a_game(calc_game)


if __name__ == '__main__':
    main()
