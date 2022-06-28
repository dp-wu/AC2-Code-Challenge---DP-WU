import random


# create a pool of letter candidates
LETTERS = ['R', 'Y', 'G', 'B', 'I', 'V']
# define list length
LEN = 4


def generate_code():
    # create a list of 4 random letters from LETTERS
    letters = [
        LETTERS[random.randint(0, 5)], 
        LETTERS[random.randint(0, 5)],
        LETTERS[random.randint(0, 5)],
        LETTERS[random.randint(0, 5)]
    ]
    return letters

def validate_guess(guess):
    result = False
    # check if input is a list (iterable)
    if not isinstance(guess, list):
        raise TypeError("Guess input needs to be a list.")
    else:
        # check if input length is valid
        if len(guess) == LEN:
            result = True
            for i in LEN:
                # check if each element is in LETTERS
                if guess[i].upper() not in LETTERS:
                    result = False
                    break
    return result

def color_count(guess, code):
    pass

def correct_pos_and_color(guess, code):
    pass

def check_guess(guess, code):
    pass

def check_win_or_lose(guess, code, num_guesses):
    pass

def get_win_percentage(wins, plays):
    pass

def format_guess_stats(guess_stats):
    pass

