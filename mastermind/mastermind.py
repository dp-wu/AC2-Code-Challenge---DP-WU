from .game import generate_code, validate_guess, color_count, correct_pos_and_color, check_guess, check_win_or_lose, get_win_percentage, format_guess_stats

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

def mastermind():
    #implement game loop here
    pass
    
