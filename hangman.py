# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter in letters_guessed:
            word_guessed = True
        else:
            word_guessed = False
            break
    return word_guessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append("_ ")
    return ''.join(guessed_word)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    not_guessed = []
    for letter in alphabet:
        if letter not in letters_guessed:
            not_guessed.append(letter)
    return ' '.join(not_guessed)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    win = False
    global current_guess
    global lives
    current_guess = ""
    
    
    print("This is Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("----------")
    while lives > 0 and not win:    
        info(lives)
        guess(input("What letter do you want to guess?"))
        print("----------")
        win = is_word_guessed(secret_word, letters_guessed)
    if  lives <= 0:
        print("Oh no! That was your last life!")
        print("Your guess was " + get_guessed_word(secret_word, letters_guessed) + " .")
        print("The secret word was " + secret_word + ".")
        print("You lose! :(")
        play_again(input("Would you like to play again? Type y/n"))
        return
    if win:
        print("Congratulations! You win!")
        play_again(input("Would you like to play again? Type y/n"))
        return
     
def info(lives):
    '''
    lives: the number of lives the user has left
    Shows the user what letters they can guess and how many lives they have 
    left.
    '''
    print("You have " + str(lives) + " lives left.")
    print("You can still guess these letters: " + str(get_available_letters(letters_guessed)))
    print("----------")
    print("This is the word so far:")
    print(get_guessed_word(secret_word, letters_guessed))
    print("----------")
    return


def guess(letter):
    if isinstance(letter, str) and letter not in letters_guessed:
        letters_guessed.append(letter.lower())
        current_guess = letter.lower()
        print("You guessed " + letter.lower() + ".")
        print(correct_guess(current_guess))
        return
    elif letter in letters_guessed:
        print("You've already guessed that letter, try again!")
        return
    else:
        print("That's not a letter, try again!")
        return
        
def correct_guess(letter):
    global lives
    if letter in secret_word:
        return "Nice job! The letter " + letter + " is in the secret word."
    else:
        lives -= 1
        return "Sorry, " + letter + " is not in the secret word."

def play_again(answer):
    global lives
    global letters_guessed
    global secret_word
    if str(answer.lower) == "y":
        lives = 6
        letters_guessed.clear()
        secret_word = choose_word(wordlist)
        hangman(secret_word)
        return
    elif str(answer.lower) == "n":
        print("Okay, thanks for playing!")
        return
    else:
        print("Sorry, I didn't understand that answer. Do you want to play again? y/n")
        print(answer)
        play_again(input())
        return

lives = 6
letters_guessed = []
secret_word = choose_word(wordlist)
hangman(secret_word)



    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
