# Coding Challenge 3, hangman.py
# Name:
# Student No:

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
from string import ascii_lowercase

WORDLIST_FILENAME = "words.txt"
SCORE_FILENAME = "scores.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):
    """
    Chooses a random word from those available in the wordlist
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
    """
    return random.choice(all_words)


# end of helper code
# -----------------------------------


def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
    """
    # TODO: Fill in your code here
    try:
        with open(WORDLIST_FILENAME, "r") as f:
            file_content = f.read()
            word_list = file_content.split(" ")
        f.close()
    except (OSError, IOError) as e:
        print(e)
        exit(0)

    print("Loading word list from file...")
    print("{} words loaded".format(len(word_list)))

    return word_list


# Load the list of words into the variable wordlist
# Accessible from anywhere in the program
# TODO: uncomment the below line once
# you have implemented the load_words() function

# wordlist = load_words()

def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    # TODO: Fill in your the code here

    for x in letters_guessed:
        word = word.replace(x, '')

    if len(word) < 1:
        return True
    else:
        return False


def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and
        spaces that represents which letters have been guessed so far.
    """
    # TODO: Fill in your code here
    current_guessed_word = ""
    for x in word:
        if x in letters_guessed:
            current_guessed_word += x
        else:
            current_guessed_word += '_ '

    return current_guessed_word


def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    # TODO: Fill in your code here
    remaining_letters = ascii_lowercase
    for letter_guessed in letters_guessed:
        remaining_letters = remaining_letters.replace(letter_guessed, '')

    return remaining_letters


def get_score(user_name):
    saved_score = None
    try:
        with open(SCORE_FILENAME, "r") as f:
            data = f.readlines()
            for line in data:
                score = line.split(", ")[0]
                name = line.split(", ")[1].strip()
                if name == user_name:
                    saved_score = score
        f.close()
    except (OSError, IOError) as e:
        print(e)
        exit(0)

    return saved_score


def save_score(user_name, score):
    saved_score = get_score(user_name)
    if saved_score is not None and saved_score:
        saved_score = int(get_score(_user_name))

    if saved_score is None:
        update_score = input("Would you like to store your score(y/n):").lower()
        if update_score == 'y':
            try:
                with open(SCORE_FILENAME, "a") as f:
                    data = str(score) + ", " + user_name + "\n"
                    f.write(data)
                f.close()
                print("Ok, your score has been saved.")
            except (OSError, IOError) as e:
                print(e)
                exit(0)
    else:
        if saved_score < score:
            update_score = input("A new personal best! Would you like to save your score(y/n):").lower()
            if update_score == 'y':
                with open(SCORE_FILENAME, "r") as f:
                    data = f.readlines()
                    for x in range(len(data)):
                        name = data[x].split(", ")[1].strip()
                        if name == user_name:
                            data[x] = str(score) + ", " + user_name + "\n"
                f.close()
                with open(SCORE_FILENAME, "w") as f:
                    f.writelines(data)
                f.close()
                print("Ok, your score has been saved.")


def show_leader_board():
    title_space = 10
    content_space = 15
    print("Score" + title_space * " " + "Name")
    print("-----------------------------------")
    try:
        with open(SCORE_FILENAME, "r") as f:
            score_data = f.readlines()
            for line in score_data:
                line = line.strip()
                score = line.split(", ")[0]
                name = line.split(", ")[1]
                space = content_space - len(score)
                print(score + space * " " + name)
        f.close()
    except (OSError, IOError) as e:
        print(e)
        exit(0)


def hangman(word):
    """
    Runs an interactive game of Hangman.

    Args:
        word: string, the word to guess.
    """
    print("Welcome to Hangman Ultimate Edition")
    print("I am thinking of a word that is {0} letters long".format(len(word)))
    print("-------------")
    # TODO: Fill in your code here

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)


# -----------------------------------

# Driver function for the program
if __name__ == "__main__":
    while True:
        menu_option = input("Do you want to Play (p) view the leaderboard (l) or quit (q): ")
        if menu_option == "p":
            _user_name = input("Please enter your name: ")
            _word_list = load_words()
            _word = choose_random_word(_word_list)
            hangman(_word)

            guess_count = 6
            _remaining_letters = ascii_lowercase
            _letters_guessed = []

            vowels = ['a', 'e', 'i', 'o', 'u']
            is_succeed = False

            while guess_count > 0:
                print("You have {} guesses left".format(guess_count))
                print("Available letters: {}".format(_remaining_letters))
                _letter_guessed = input("Please guess a letter: ").lower()

                if _letter_guessed.isalpha() is False:
                    print("guess is invalid")
                    guess_count -= 1
                    print("-------------")
                    continue

                _letters_guessed.append(_letter_guessed)
                _remaining_letters = get_remaining_letters(_letters_guessed)
                _guessed_word = get_guessed_word(_word, _letters_guessed)

                letters_guessed_for_compare = _letters_guessed.copy()
                letters_guessed_for_compare.pop()
                if _letter_guessed in letters_guessed_for_compare:
                    print("Oops! You've already guessed that letter: {}".format(_guessed_word))
                    print("-------------")
                    continue

                if _letter_guessed in _word:
                    print("Good guess: {}".format(_guessed_word))
                    if is_word_guessed(_word, _letters_guessed):
                        is_succeed = True
                        print("-------------")
                        break
                else:
                    if _letter_guessed in vowels:
                        guess_count -= 2
                    else:
                        guess_count -= 1
                    print("Oops! That letter is not in my_word: {}".format(_guessed_word))

                print("-------------")
            if is_succeed:
                _score = guess_count * len(_word)
                print("Congratulations, you won!")
                print("Your total score for this game is: {}".format(_score))

                save_score(_user_name, _score)
            else:
                print("Sorry, you ran out of guesses. The word was: {}".format(_word))
        elif menu_option == "l":
            show_leader_board()
        elif menu_option == "q":
            print("Thanks for playing, goodbye!")
            exit(0)
        else:
            print("Invalid mode")
