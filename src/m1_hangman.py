"""
Hangman.

Authors: Tristen Foisy, Sam Hedrick, Tommy Hoevener
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    print("Game has started.")
    word = random_word()
    min_length = length()
    final_word = check_length(min_length, word)
    # print(final_word)
    # letter = guess_a_letter()
    # print(check_guess(letter, final_word))
    repeat_guesses(final_word)


def random_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(0, len(words))
    word = words[r]
    return word


def length():
    string = input('Input a length less than 23 for the secret word:')
    integer = int(string)
    return integer


def check_length(min_length, word):
    final_word = word
    while True:
        if len(final_word) < min_length:
            final_word = random_word()
        else:
            print('I am thinking of a word...')
            break
    return final_word


def guess_a_letter():
    letter = input('Guess a letter:')
    return letter


def check_guess(letter, final_word):
    for k in range(len(final_word)):
        if letter == final_word[k]:
            return 'Correct!', k, letter
    return 'Wrong!', None, None


def repeat_guesses(final_word):
    number_wrong = 0
    while True:
        if number_wrong < 3:
            letter = guess_a_letter()
            response, index, letter = check_guess(letter, final_word)
            print(response)
            if response == 'Wrong!':
                number_wrong = number_wrong + 1
        elif number_wrong == 3:
            print('YOU LOSE!')
            print('The secret word was:', final_word)
            break


main()
