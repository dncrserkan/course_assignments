import random


# Each of our text files contains 1000 words
LISTSIZE = 1000     # change 1 for testing

# Values for colors and score 
EXACT = 2   # right letter, right place
CLOSE = 1   # right letter, wrong place
WRONG = 0   # wrong letter

# ANSI color codes for boxed in letters
GREEN  = "\033[42m"
YELLOW = "\033[43m"
RED    = "\033[41m"
RESET  = "\033[0m"


def main():
    """ MAKE IT READY """
    wordsize = get_wordsize()

    # Open correct file, each file has exactly LISTSIZE words
    wl_filename = str(wordsize) + ".txt"
    try:
        wordlist = open(wl_filename, "r")
    except FileNotFoundError:
        print(f"Error opening file {wl_filename}")

    # Load word file into an list of size LISTSIZE
    options = []
    for word in wordlist.readlines(LISTSIZE):
        options.append(word.strip())

    # Pseudorandomly select a word for this game
    choice = random.choice(options)

    wordlist.close()

    # Allow one more guess than the lenght og the word
    guesses = wordsize + 1

    # Print greeting, using ANSI color codes to demostrate
    print(f"{GREEN}This is WORDLE50{RESET}")
    print(f"You have {guesses} tries to guess the {wordsize}-letter word I'm thinking of")


    """ MAIN LOOP """
    # Main game loop, one iteration for each guesses
    for i in range(guesses):
        # Obtain user's guess
        guess = get_guess(wordsize)

        # Set all elements of status array initially to 0, aka WRONG
        status = [0 for _ in range(wordsize)]

        # Calculate  score for the guess
        score = check_word(guess, wordsize, status, choice)
        print(f"Guess {i+1}: ", end="")

        # Print the guess
        print_word(guess, wordsize, status)

        #If they gueessed it exactly right, set terminate loop
        if score == (EXACT * wordsize):
            print('You won!')
            break
            
        else:
            guesses -= 1
            if guesses == 0:
                print("You run out guesses...")
                print(f"The word was: {choice}")


def get_wordsize():
    while True:
        test = ("5", "6", "7", "8")
        print("Choose lenght of word you wanna guess.")
        temp = input("Wordsize: ")
        
        if temp in test:
            return int(temp)
        else:
            print("You can only choose one of 5-6-7-8")


def get_guess(wordsize:int) -> str:
    while True:
        temp = input(f"Input a {wordsize}-letter word: ")
        test = ""

        if len(temp) != wordsize:
            continue

        for char in temp:
            if char.isascii() and char.isalpha():
                test += char
            else:
                break
        
        if len(test) == wordsize:
            return temp


def check_word(guess:str, wordsize:int, status:list, choice:str) -> int:
    ''' compare guess with choice and score points as appropriate, storing points in status '''
    score = 0
    for i in range(wordsize):
        if guess[i] == choice[i]:
            status[i] = 2
        elif guess[i] in choice:
            status[i] = 1
        else:
            status[i] = 0
    return sum(status)

    
def print_word(guess:str, wordsize:int, status:list) -> None:
    ''' print word character-for-character with correct color coding, then reset terminal font to normal '''
    for i in range(wordsize):
        if status[i] == EXACT:
            print(f"{GREEN}{guess[i]}{RESET}", end="")
        elif status[i] == CLOSE:
            print(f"{YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(f"{RED}{guess[i]}{RESET}", end="")
    print("")


if __name__ == "__main__":
    main()