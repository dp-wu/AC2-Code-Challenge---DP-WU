import random


# create a pool of letter candidates
LETTERS = ['R', 'Y', 'G', 'B', 'I', 'V']
# define list length
LEN = 4
# max attempt
MAX_ATTEMPT = 8


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
    count = dict()
    result = 0
    # create a answer dictionary: {color: [codecount, guesscount]}
    for i in code:
        if i in count.keys():
            count[i][0] += 1
        else:
            count[i] = [1, 0]
    for j in guess:
        if j in count.keys():
            count[j][1] += 1
    # calculate total correct color guessed
    for k in count.values():
        result += min(k)
    return result

def correct_pos_and_color(guess, code):
    pass

def check_guess(guess, code):
    pass

def check_win_or_lose(guess, code, num_guesses):
    result = True
    # check if results are matching
    for i in range(LEN):
        if guess[i] != code[i]:
            result = False
            break
    # check if guesses within limit
    if result == True and num_guesses <= MAX_ATTEMPT:
        result = True
    elif result == False and num_guesses > MAX_ATTEMPT:
        result = False
    else:
        result = None
    return result

def get_win_percentage(wins, plays):
    pass

def format_guess_stats(guess_stats):
    pass
