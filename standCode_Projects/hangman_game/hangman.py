"""
File: hangman.py
Name:李安哲
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Main function that runs the hangman game.
    """
    ans = random_word()
    s = answer_to_dash(ans)
    n_turns = N_TURNS
    while s != ans:
        input_ch = str(input('Your guess: ')).upper()  # Ensure input is uppercase
        if not input_ch.isalpha():   # Check input is alphabet
            print('illegal format."')
        elif len(input_ch) != 1:  # Check input is a single character
            print('illegal format."')
        else:
            if ans.find(input_ch) != -1:  # Guess correct
                print('You are correct!')
                s = replace(ans, s, input_ch)
                if s == ans:
                    print('You Win!!')
                    break
            else:
                print('There is no '+input_ch+"'s in the word.")
                n_turns += -1
                if n_turns == 0:
                    print('You are completely hung :(')
                    break
            print("The word looks likes: " + s)
            print("You have " + str(n_turns) + ' wrong guesses left.')
    print('The answer is: '+ans)


def replace(ans, old_s, input_ch):
    """
    :param ans: str, the answer
    :param old_s: str, the string before guessing
    :param input_ch: str, the word that was guessed
    :return: str, the new string after guessing correctly
    """
    new_s = ''
    for i in range(len(ans)):
        if ans[i] == input_ch:
            new_s += input_ch
        else:
            new_s += old_s[i]
    return new_s


def answer_to_dash(ans):
    """
    :param ans: str, random answer
    :return: str, A dash with the same number of characters as the answer.
    """
    s = ''
    for i in range(len(ans)):
        s += '_'
    return s


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
