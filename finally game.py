import os


MAX_TRIES = 6

COL_1 = "\033[94m"
COL_2 = "\033[31m"
COL_3 = "\033[91m"
COL_4 = "\033[93m"
END_COL = "\033[0m"


def opening_screen():
    """print the opening screen."""

    HANGMAN_ASCII_ART = f"""{COL_3}  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/  {END_COL}"""

    USER_NAME = os.getenv('username')

    print(HANGMAN_ASCII_ART, f"\n{COL_1}{MAX_TRIES} \n\nHello {COL_4}{USER_NAME}!{END_COL} \n")


def vaild_path():
    """ Get a input - file path from user and checks that the path is vaild
    :return:  var of open text file

    """
    path_vaild = False
    while not path_vaild:
        file_path = r"" + input(f"{COL_1}Enter file path:")
        try:
            file_path = open(r"" + file_path)
            path_vaild = True
        except:
            print(f"{COL_3}Invalid path!")

    return file_path


def vaild_index():
    index_vaild = False
    while not index_vaild:
        try:
            index = (int(input(f"{COL_1}Please enter index:")))
            index_vaild = True
        except:
            print(f"{COL_3}Invalid index!")

    return index


def choose_word():
    file = vaild_path()
    word_list = file.read().split()
    index = vaild_index()
    index = index % len(word_list) - 1

    return word_list[index]


def check_valid_input(letter_guessed, old_letters_guessed):
    """

    :param letter_guessed:
    :param old_letters_guessed:
    :return:
    """
    return letter_guessed.isalpha() and len(letter_guessed) == 1 and letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        old_letters_guessed.sort()
        return True
    else:
        print(f"{COL_3}X\n", "you already guessed:\n " + " -> ".join(old_letters_guessed) if len(old_letters_guessed) > 0 else "")
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    st = ""
    for i in secret_word:
        if i in old_letters_guessed:
            st += i
        else:
            st += "_"

    print("\n\t", " ".join(st))


def wrong_choice(secret_word, letter_guessed):
    return letter_guessed not in secret_word


def check_win(secret_word, old_letters_guessed):
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True


def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {"trie 0":

    "       x-------x ",

                          "trie 1": """ 
            x-------x
            |
            |
            |
            |
            |""",

                          "trie 2": """
            x-------x
            |       |
            |       0
            |
            |
            |""",

                          "trie 3": """
            x-------x
            |       |
            |       0
            |       |
            |
            |""",

                          "trie 4": """
            x-------x
            |       |
            |       0
            |      /|\\
            |
            |""",

                          "trie 5": """
            x-------x
            |       |
            |       0
            |      /|\\
            |      /
            |""",

                          "trie 6": """
            x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            | """}

    print(HANGMAN_PHOTOS["trie " + str(num_of_tries)])


def main():
    os.system("cls")
    opening_screen()
    print(COL_1)
    SECRET_WORD = choose_word().lower()

    old_letters_guessed = []
    num_of_tries = 0
    print(COL_4)
    print_hangman(num_of_tries)
    print(COL_1)
    show_hidden_word(SECRET_WORD, old_letters_guessed)

    while num_of_tries < MAX_TRIES:
        print(COL_4)
        print_hangman(num_of_tries)
        print(COL_1)
        show_hidden_word(SECRET_WORD, old_letters_guessed)
        user_guess = input("Guess a letter:").lower()
        if try_update_letter_guessed(user_guess, old_letters_guessed):
            if wrong_choice(SECRET_WORD, user_guess):
                num_of_tries += 1
                print(":(")
            print(COL_4)
            print_hangman(num_of_tries)
            print(COL_1)
            show_hidden_word(SECRET_WORD, old_letters_guessed)

            if check_win(SECRET_WORD, old_letters_guessed):
                print("you win!")
                break
            else:
                print("you'r left:", MAX_TRIES - num_of_tries)
                if num_of_tries == MAX_TRIES:
                    print("\tYou lose ):\n\tthe word is:\n\t", " ".join(SECRET_WORD))


if __name__ == '__main__':
    main()
