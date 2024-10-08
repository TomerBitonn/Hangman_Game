import hangman_functions
import constants


def main():

    # variables
    old_letters_guessed = []
    num_of_tries = 1
    
    # open screen
    hangman_functions.hangman_open_screen()
       
    # secret word index
    index = hangman_functions.get_index()
    if index == 1:
        index = 0
    
    secret_word = hangman_functions.choose_word(constants.FILE_PATH, index)
    
    hangman_functions.print_hangman(num_of_tries)
    print(len(secret_word) * " _ ")
    
    # game loop
    while num_of_tries < 7:
        
        letter_guessed = input("Guess a letter: ")
      
        bool_type, old_letters_guessed = hangman_functions.try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if bool_type and letter_guessed in secret_word:
            hangman_functions.show_hidden_word(secret_word, old_letters_guessed)
                
        elif letter_guessed == "quit":  # rage quit
            break

        elif not bool_type or letter_guessed not in secret_word:
            print("\n):") 
            num_of_tries += 1
            hangman_functions.print_hangman(num_of_tries)
            print("\n")
            hangman_functions.show_hidden_word(secret_word, old_letters_guessed)
            
        win_lose_check = hangman_functions.check_win(secret_word, old_letters_guessed)
        if win_lose_check:
            print("\nWOW YOU WIN!\n")
            num_of_tries = 7
            
        elif (not win_lose_check) and (num_of_tries == 7):
            print(f"\nYou LOSE!\n\nThe word is: '{secret_word}'\n")


if __name__ == "__main__":
    main()
