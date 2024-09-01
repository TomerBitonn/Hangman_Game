import constants


def hangman_open_screen():
    print(constants.HANGMAN_ASCII_ART)
    print(f"Number of lives: {constants.MAX_TRIES}")
    print("\nLet's start!\n")


def print_hangman(num_of_tries):
    # prints the hangman position
    print(constants.HANGMAN_PHOTOS[num_of_tries])
    
    
def choose_word(file_path, index):
    # choosing the secret word from the text file
    with open(file_path, "r") as words_list:  # open the file as a new file named "words list"
        words = words_list.read()  # read the file "words list" and define it as a new file
        words_into_list = words.replace('\n', ' ').split(' ')  # replace the new lines with spaces and make it a list
        new_words_list = []  # create a new list
        
        for word in words_into_list:
            if word not in new_words_list:
                new_words_list.append(word)
                
        while index > len(new_words_list):
            index -= len(new_words_list)
            
    secret_word = str(new_words_list[index])
    return secret_word
    
    
def show_hidden_word(secret_word, old_letters_guessed):
    # show everytime one letter from the secret word
    for letter in secret_word:
        if letter not in old_letters_guessed:
            secret_word = secret_word.replace(letter, " _ ")
    print(secret_word)
    
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    check_letter = None
    # check the letter guessed
    if ((len(letter_guessed) == 1) and letter_guessed.isalpha()
            and (letter_guessed.lower() not in old_letters_guessed)):
        check_letter = True
        old_letters_guessed.append(letter_guessed)
        
    elif ((len(letter_guessed) >= 2) or (not letter_guessed.isalpha())
          or (letter_guessed.lower() in old_letters_guessed)):
        check_letter = False
        print("X\n")
        print(" -> ".join(sorted(old_letters_guessed)))
    return check_letter, old_letters_guessed


def check_win(secret_word, old_letters_guessed):
    # check if the player won
    counter = 0
    for i in range(len(secret_word)):
        for j in range(len(old_letters_guessed)):
            if old_letters_guessed[j] == secret_word[i]:
                counter += 1
                
    if counter == len(secret_word):
        return True
    else:
        return False
    

def get_index():
    # get an index from the user and check if it's an integer
    while True:
        index = input("Enter a random number: ")
        try:
            number = int(index)
            return number
        except ValueError:
            print("Error: That's not a valid integer. Please try again.")
