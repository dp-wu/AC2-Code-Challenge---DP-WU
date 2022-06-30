from .game import generate_code, validate_guess, color_count, correct_pos_and_color, check_guess, check_win_or_lose, get_win_percentage, format_guess_stats


# create a pool of letter candidates
LETTERS = ['R', 'Y', 'G', 'B', 'I', 'V']
# define list length
LEN = 4
# max attempt
MAX_ATTEMPT = 8


# These functions allow you to print a string s in the stated colors. Using them is NOT required
def print_red(s):
    return '\033[31m' + s + '\033[0m'

    
def print_yellow(s):
    return '\033[33m' + s + '\033[0m'


def print_green(s):
    return '\033[32m' + s + '\033[0m'


def print_blue(s):
    return '\033[36m' + s + '\033[0m'


def print_indigo(s):
    return '\033[34m' + s + '\033[0m'


def print_violet(s):
    return '\033[35m' + s + '\033[0m'



def greet_and_gen_code():
    """
    print greetings for current round
    return secret code generated for current round
    """
    code = generate_code() # generate new secret code
    print(print_blue("Generating a new code..."))
    print(print_blue("New code generated: ****"))
    print(print_blue("Guess the code! Each character in the code is one of the following letters: R, Y, G, B, I, V"))
    return code


def current_attempt(code, num_guesses):
    """
    validate current attempt
    return check info and whether won current attempt or not
    """
    print(print_blue("Guess the code:"))
    guess = input("####user input: ")
    print("You guessed: {}".format(guess))
    # reformat string into a list of characters and validate input
    guess = list(guess)
    # assert validate_guess(guess) == True
    # check guess (correct_pos_and_color, incorrect_pos_correct_color)
    check = check_guess(guess, code)
    # result shows True, False or None
    result = check_win_or_lose(guess, code, num_guesses)
    return check, result


def show_stats(games_played, wins, guess_stats):
    # print current round statistics
    print(print_indigo("STATISTICS"))
    print(print_indigo("Games Played: {}".format(games_played)))
    print(print_indigo("Win %: {}".format(get_win_percentage(wins, games_played))))
    print(print_indigo("Guess Distribution:"))

    stats = format_guess_stats(guess_stats)
    for i in range(MAX_ATTEMPT):
        print(print_indigo("{}| {}".format(i+1, stats[i])))


def mastermind():
    print(print_yellow("Welcome to Mastermind!"))
    # total games played
    games_played = 0
    # total games won
    wins = 0
    # stats of all sessions
    guess_stats = {key+1: 0 for key in range(MAX_ATTEMPT)}
    
    # play one round of game
    while True:
        # game data
        games_played += 1
        attempts = 0       
        # generate new code
        code = greet_and_gen_code()
        
        # get user guesses
        while True:
            attempts += 1
            if attempts <= MAX_ATTEMPT:
                # get result info
                check, result = current_attempt(code, attempts)
                if result == True:
                    # if guessed correctly for all 4 pegs in positions and colors
                    print(print_green(
                        "Congratulations! You guessed the secret code!"))
                    # populate guess stats
                    guess_stats[attempts] += 1
                    wins += 1
                    break
                else:
                    print(check)
            else:
                print(print_red("You lost 😥 Better luck next time!"))
                break

        # print stats
        show_stats(games_played, wins, guess_stats)
        
        # ask if play another round
        print(print_violet("Should we play another round?"))
        play_again = input("Enter y to replay, any other character to exit: ")
        if play_again != 'y':
            break
