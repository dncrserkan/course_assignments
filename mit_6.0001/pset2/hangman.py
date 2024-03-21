import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as file:
        line = file.readline()
        wordlist = line.split()
        print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    shown_word = ''
    for char in secret_word:
        if char in letters_guessed:
            shown_word += char
        else:
            shown_word += '_ '
    return shown_word


def get_available_letters(letters_guessed):
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
    return available_letters


def show_score(guess_counter, secret_word):
    unique_letters = []
    for char in secret_word:
        if char not in unique_letters:
            unique_letters.append(char)
    score = guess_counter * len(unique_letters)
    print("Your total score for this game is:", score)


def hangman(secret_word):
    letters_guessed = []
    warning_counter = 3
    guess_counter = 6
    
    print('Welcome to the game Hangman !')
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have {} warnings left".format(warning_counter))
    print(get_guessed_word(secret_word, letters_guessed))
    
    while True:
    
        if guess_counter <= 0:
            print("\n Sorry, you ran out of guesses! The word was", secret_word)
            input('\n Press enter to continue \n ')
            break
        
        print("\n", '-' * 15, "\n")
        print("You have", guess_counter, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        letter_guessed = input("Please guess a letter: ").lower()
        
        if not letter_guessed.isalpha():
            warning_counter -= 1
            if warning_counter <= 0:
                guess_counter -= 1
                print("You run out of warnings! So you lose one guess!")
            print(f"That is not a valid letter. You have {warning_counter} warnings left:", get_guessed_word(secret_word, letters_guessed))
        else:
            if letter_guessed in letters_guessed:
                warning_counter -= 1
                if warning_counter <= 0:
                    guess_counter -= 1
                    print("You have no warnings left so you lose one guess!")
                print(f"Ooops! You've already guessed that letter. You have {warning_counter} warnings left", get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(letter_guessed)
                if letter_guessed in secret_word:
                    if is_word_guessed(secret_word, letters_guessed):
                        print(secret_word)
                        print('Congratulations, you won!')
                        show_score(guess_counter, secret_word)
                        input('\n Press enter to continue \n ')
                        break
                    print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
                else:
                    if letter_guessed in 'aeiou':
                        guess_counter -= 2
                    else:
                        guess_counter -= 1
                    print("Ooops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))


def match_with_gaps(my_word, other_word):
    for i in range(len(other_word)):
        if other_word[i] == my_word[i]:
            continue
        elif my_word[i] == "_" and other_word[i] not in my_word:
            continue
        else:
            return False
    return True


def show_possible_matches(my_word):
    my_word = my_word.replace(" ", "")
    matched_words = []
    for word in wordlist:
        if len(word) > len(my_word):
            # no need to go any further
            break
        if len(word) == len(my_word):
            if match_with_gaps(my_word, word):
                matched_words.append(word)
    if len(matched_words) == 0:
        print("No matches found")
    else:
        print(*matched_words)


def hangman_with_hints(secret_word):
    letters_guessed = []
    warning_counter = 3
    guess_counter = 6
    
    print('Welcome to the game Hangman W.H.!')
    print("In this version you can display possible words by enter *")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have {} warnings left".format(warning_counter))
    print(get_guessed_word(secret_word, letters_guessed))
    
    while True:
    
        if guess_counter <= 0:
            print("\n Sorry, you ran out of guesses! The word was", secret_word)
            input('\n Press enter to continue \n ')
            break
        
        print("\n", '-' * 15, "\n")
        print("You have", guess_counter, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        letter_guessed = input("Please guess a letter: ").lower()
        
        if letter_guessed == '*':
            print("Possible word matches are:")
            my_word = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(my_word)

        elif not letter_guessed.isalpha():
            warning_counter -= 1
            if warning_counter <= 0:
                guess_counter -= 1
                print("You run out of warnings! So you lose one guess!")
            print(f'That is not a valid letter. You have {warning_counter} warnings left:',get_guessed_word(secret_word, letters_guessed))
        
        else:
            if letter_guessed in letters_guessed:
                warning_counter -= 1
                if warning_counter <= 0:
                    guess_counter -= 1
                    print("You have no warnings left so you lose one guess!")
                print(f"Ooops! You've already guessed that letter. You have {warning_counter} warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(letter_guessed)
                if letter_guessed in secret_word:
                    if is_word_guessed(secret_word, letters_guessed):
                        print(secret_word)
                        print('Congratulations, you won!')
                        show_score(guess_counter, secret_word)
                        input('\n Press enter to continue \n')
                        break
                    print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
                else:
                    if letter_guessed in 'aeiou':
                        guess_counter -= 2
                    else:
                        guess_counter -= 1
                    print("Ooops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))


wordlist = load_words()

# if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)



# while True:
#     secret_word = choose_word(wordlist)
#     print("1 to play hangman")
#     print("2 to play hangman with hints")
#     print("3 for exit")
#     user_choice = input("\n Which version do you want to play: ")
#     if user_choice == "1":
#         hangman(secret_word)
#     elif user_choice == "2":
#         hangman_with_hints(secret_word)
#     elif user_choice == "3":
#         break
