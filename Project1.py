import random
#from colorama import init
#init()
from colorama import Fore
from colorama import Style

class Letter:
    def __init__(self, color, letter):
        self.color = color
        self.letter = letter

f = open("fiveletterwords.txt", "r")
content = f.read()
words_list = open("fiveletterwords.txt").read().split()

def select_word():
    return random.choice(words_list).upper()

#print(selected_word)
def print_menu():
    print('\nThe object of the game, Wordle, is to guess the hidden word in 6 guesses or less. \n'
    f'After each guess: \nEach correct letter turns {Fore.GREEN}GREEN{Style.RESET_ALL}. \n' 
    f'Each correct letter in the wrong place turns {Fore.LIGHTYELLOW_EX}YELLOW{Style.RESET_ALL}. \n'
    f'Incorrect letters turn {Fore.RED}RED{Style.RESET_ALL}.')

def get_user_input(turn):
    return input(f'\nType a 5 letter word and hit enter! turn:{turn+1}/6\n').upper()

def check_word(user_input, selected_word) :
    if user_input == selected_word:
        return("Correct")
# Check letters separately
    letter_list = [] # list to return color and letters
    for k in range(0, 5):
        l = Letter(Fore.RED, user_input[k])
        for j in range(0,5):
            #print(k, j, user_input[k], selected_word[k])
            if user_input[k] == selected_word[k]:
                l.color = Fore.GREEN
            elif user_input[k] == selected_word[j]:
                l.color = Fore.LIGHTYELLOW_EX
        letter_list.append(l) #to control and return user input

    return(letter_list)

def ask_play_again():
    y = input("\nWould you like to play again? Please write 'Y' for yes, 'N' for no \n").upper()
    if y == "Y":
        return True
    else:
        return False

def start_again():
    again = ask_play_again()
    if again:
        game()
    else:
        print("It's sad to see you go :( Come back again later! :)")
        exit()

def game():
# Main loop
    selected_word = select_word()
    print_menu()
    print(selected_word)
    i = 0
    while i < 6:
        user_input = get_user_input(i)
        if len(user_input) != 5:
            print("Incorrect, try a 5 letter word")
        else:
            result = check_word(user_input, selected_word)
            i = i + 1
            if result == "Correct":
                print("Congratulations, you won!")
                start_again()

            print(f'{result[0].color}{result[0].letter}{result[1].color}{result[1].letter}{result[2].color}{result[2].letter}{result[3].color}{result[3].letter}{result[4].color}{result[4].letter}{Style.RESET_ALL}')

    print("You lose!")
    start_again()

game()

    #To DO:  2) write remaining turns, 4) If only one letter i.e "s" in selected_word,
    # one "s" should be yellow or green, second "s" red. 5) create a view