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

WORDLIST_FILENAME = "C:\\Users\innas\Desktop\Python\words.txt"


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
    for i in secret_word :
      if (i not in letters_guessed): return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letter_list = []
    for i in secret_word:
      if (i in letters_guessed):
        letter_list.append(i)
      else: 
        letter_list.append('_')
    return''.join(letter_list)






def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = []
    all_list_letters = string.ascii_lowercase
    for i in all_list_letters:
      if (i not in letters_guessed):
        available_letters.append(i)
    return "".join(available_letters)



    

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
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
      print("You have", guesses, "guesses left.")
      print("Available letters:", get_available_letters(letters_guessed))
      guess = input("Please guess a letter - ")
      if len(guess)==1 and str.isalpha(guess):
        guess = str.lower(guess)
        if guess in letters_guessed:
          if warnings != 0:
            warnings -= 1
            print("Oops! You've already guessed that letter. You have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
          else:
            guesses -= 1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        else:
          letters_guessed.append(guess)
          if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
          else:
            if guess in ['a', 'e', 'i', 'o', 'u']:
              guesses -= 2
            else:
              guesses -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
      else:
        if warnings != 0:
          warnings-= 1
          print("Oops! That is not valid letter. You have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        else:
          guesses -= 1
          print("Oops! That is not valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
      print("-----------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
      print("Congratulations, you won! Your total score for this game is:", guesses * len(set(secret_word)))
    else:
      print("Sorry, you ran out of guesses. The word was else")




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
    my_word = list(my_word.replace(' ', ''))
    other_word = list(other_word )

    if len(my_word) != len(other_word): 
      return False 
    else:  
      for i in range (len(my_word)):
        if my_word[i] != '_' and my_word [i] != other_word [i]:
          return False
      for i in range(len(my_word)): 
        f = i + 1 
        for f in range(len(my_word)):
          if other_word [i] == other_word [f] and my_word [i] != my_word [f]: 
            return False 
    return True







def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for i in wordlist:
      if match_with_gaps(my_word, i):
        matches.append(i)
    if len(matches) == 0:
      print("No matches found")
    else:
      print('Possible word matches are: ', end = ' ')
      for j in matches:
        print(j, end=" ")
    print(" ")

    
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
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-----------------------------------")
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
      print("You have", guesses, "guesses left.")
      print("Available letters:", get_available_letters(letters_guessed))
      guess = input("Please guess a letter - ")
      if guess == '*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      elif len(guess)==1 and str.isalpha(guess):
        guess = str.lower(guess)
        if guess in letters_guessed:
          if warnings != 0:
            warnings -= 1
            print("Oops! You've already guessed that letter. You have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
          else:
            guesses -= 1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        else:
          letters_guessed.append(guess)
          if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
          else:
            if guess in ['a', 'e', 'i', 'o', 'u']:
              guesses -= 2
            else:
              guesses -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
      else:
        if warnings != 0:
          warnings-= 1
          print("Oops! That is not valid letter. You have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        else:
          guesses -= 1
          print("Oops! That is not valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
      print("-----------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
      print("Congratulations, you won! Your total score for this game is:", guesses * len(set(secret_word)))
    else:
      print("Sorry, you ran out of guesses. The word was else")

    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    print('----------------')
    print('Choose the version of the game:')
    print('1 - hangman')
    print('2 - hangman with hints')
    secret_word = choose_word(wordlist)
    print('----------------')
    c = int(input())
    print('----------------')
    if c == 1:
      hangman(secret_word) 
    else:
      hangman_with_hints(secret_word)
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
