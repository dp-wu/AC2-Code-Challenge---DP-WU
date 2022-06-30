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
        LETTERS[random.randint(0, 5)], LETTERS[random.randint(0, 5)],
        LETTERS[random.randint(0, 5)], LETTERS[random.randint(0, 5)]
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
            for i in range(LEN):
                # check if each element is in LETTERS
                if guess[i].upper() not in LETTERS:
                    result = False
                    break
    return result


def color_count(guess, code):
    count = dict()
    result = 0
    # create a answer dictionary: {color: [codecount, guesscount]}
    """
    I think one of the given examples is incorrect:
    guess = ['R','R','R','B'], code = ['B','I','R','R'], output = 2
    I believe the result should be 3, because in the description:
    - A letter that appears more times in guess than it appears in code is counted
        the number of times it appears in code
    - A letter that appears fewer times in guess than it appears in code is counted
        the number of times it appears in guess
    The 'R' should be counted twice, and the 'B' counted once, total add up to 3
    """
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
    """
    again i think one of the examples is having incorrect output:
    guess: ['R','I','Y','G'], code: ['R','I','Y','G'], output: 2
    the output should be 4
    """
    result = 0
    for i in range(LEN):
        # count number of pegs patched both position and color
        if guess[i] == code[i]:
            result += 1
    return result


def check_guess(guess, code):
    # number of correct position and color pegs
    result0 = correct_pos_and_color(guess, code)
    # number of incorrect position but correct color pegs
    result1 = color_count(guess, code) - result0
    return result0, result1


def check_win_or_lose(guess, code, num_guesses):
    """
    Wave 2 line 85 doesn't pass, i think the description given is incorrect:
    - Returns True if the user has won the game: guess and code are the same and
        num_guesses is less than or equal to 8 => [same and <=8]=True
    - Returns False if the user has lost the game: if guess and code are not the
        same and num_guesses is more than 8 => [!same and > 8]=False
    - Returns None otherwise - the game is still in progress => [otherwise]=None
    test case line 85:
        guess = ['R','B','B','V']
        code = ['R','B','B','V']
        num_guesses = 9
        assert result is False
    [same and >8] => does not qualify for True, does not qualify for False
    Hence if the tests are correct, then the descripion is incorrect
    """
    #result = None
    # check if results are matching
    #if correct_pos_and_color(guess, code) == LEN:
    #    result = True

    # check if guesses within limit
    #if result == True and num_guesses <= MAX_ATTEMPT:
    #    result = True
    #elif result == False and num_guesses > MAX_ATTEMPT:
    #    result = False
    #else:
    #    result = None
    if num_guesses > MAX_ATTEMPT:
        result = False
    else:
        if correct_pos_and_color(guess, code) == LEN:
            result = True
        else:
            result = None
    return result


def get_win_percentage(wins, plays):
    # result format: 75 means 75%
    result = 0
    if plays > 0:
        result = wins * 100 // plays
    return result


def format_guess_stats(guess_stats):
    # populate list with empty strings
    result = [''] * MAX_ATTEMPT
    if guess_stats:
        for k, v in guess_stats.items():
            # modify guess stats at corresponding index
            result[k-1] = 'X' * v
    return result
