#!/usr/bin/env python
import prompt
from brain_games.even_number import check_number


def main():
    # Welcome gamer
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # game
    check_number(name)


if __name__ == '__main__':
    main()
