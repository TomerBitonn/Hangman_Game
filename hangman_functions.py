import random
import constants


def hangman_open_screen():
    print(constants.HANGMAN_ASCII_ART)
    print( f"Number of tries: {constants.MAX_TRIES}")
    print("\nLet's start!\n")


def print_hangman(num_of_tries):
    """prints the hangman position"""
    print(constants.HANGMAN_PHOTOS[num_of_tries])
    return
    
    
def choose_word(file_path, index):
    """Choosing a secret word from a text file.
    :file_path: path of the text file
    :index: index of the word from the file
    :file_path type: str 
    :index type: int 
    :return: secret word
    :rtype: tuple 
    """
    with open(file_path, "r") as words_list: #open the file as a new file named "words list"
        words = words_list.read() #read the file "words list" and define it as a new file
        words_into_list = words.replace('\n', ' ').split(' ') #replace the new lines with spaces and make it a list
        new_words_list = [] #create a new list
        
        for word in words_into_list:
            if word not in new_words_list:
                new_words_list.append(word)
                
        while index > len(new_words_list):
            index -= len(new_words_list)
            
    secret_word = str(new_words_list[index])
    return secret_word
    
    
def show_hidden_word(secret_word, old_letters_guessed):
    """The function recieve a word and a list of letters,
    ant return a word with a letters from the list.
    :secret_word: the word the player need to guess
    :old_letters_guessed: list of the letters the player guessed
    :secret_word type: str
    :old_letters_guessed type: list
    :return: a word with letters from the list 
    :rtype: str 
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            secret_word = secret_word.replace(letter, " _ ")
    return print(secret_word)
    
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """If the recieved value is ok, it will be added to 
    the old_letters_guessed list. If not, the function will print X.
    :letter_guessed: recievd value from the player
    :old_letters_guessed: list with all of the guesswork
    :letter_guessed type: str
    :old_letters_guessed type: list
    :return: True, False and list of guessed letters
    :rtype: bool, str, list 
    """
    if (len(letter_guessed) == 1) and letter_guessed.isalpha() \
    and (letter_guessed.lower() not in old_letters_guessed):
        check_letter = True
        old_letters_guessed.append(letter_guessed)
        
    elif (len(letter_guessed) >= 2) or (letter_guessed.isalpha() == False) \
    or (letter_guessed.lower() in old_letters_guessed):
        check_letter = False
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
    return check_letter, old_letters_guessed


def check_win(secret_word, old_letters_guessed):
    """This function check if the player won or not.
    :secret_word: word the player need to guess
    :old_letters_guessed: letters the player guessed
    :secret_word type: str
    :old_letters_guessed type: list
    :return: True or False
    :rtype: bool
    """
    counter = i = j = 0 
    for i in range(len(secret_word)):
        for j in range(len(old_letters_guessed)):
            if old_letters_guessed[j] == secret_word[i]:
                counter += 1
                
    if counter == len(secret_word):
        return True
    else:
        return False