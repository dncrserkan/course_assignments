import math
import random


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,
    '*':0
}

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    wordlist = []
    with open(WORDLIST_FILENAME, 'r') as file:
        for line in file:
            wordlist.append(line.strip().lower())

    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    sum_of_letters = 0
    for char in word:
        sum_of_letters += SCRABBLE_LETTER_VALUES.get(char.lower(), 0)
    length_part = max((7 * len(word)) - (3 * (n - len(word))), 1)
    return sum_of_letters * length_part


def display_hand(hand):
    for letter in hand:
        for i in range(hand[letter]):
            print(letter, end=' ')
    print()


def deal_hand(n):
    hand = {'*':1, }
    num_vowels = math.ceil(n/3) - 1
    
    for _ in range(0, num_vowels):
        temp = random.choice(VOWELS)
        hand[temp] = hand.get(temp, 0) + 1
    
    for _ in range(num_vowels + 1, n):    
        temp = random.choice(CONSONANTS)
        hand[temp] = hand.get(temp, 0) + 1
    
    return hand


def update_hand(hand, word):
    new_hand = hand.copy()
    for char in word.lower():
        if new_hand.get(char, 0) > 1:
            new_hand[char] -= 1
        elif new_hand.get(char, 0) == 1:
            new_hand.pop(char)
    return new_hand


def is_valid_word(word, hand, word_list):
    if '*' in word:
        for char in VOWELS:
            changed_word = word.replace('*', char)
            changed_hand = hand.copy()
            changed_hand[char] = changed_hand.get(char, 0) + 1
            changed_hand.pop('*')
            if is_valid_word(changed_word, changed_hand, word_list):
                return True
            
    temp_word = word.lower()
    hand_copy = hand.copy()

    for char in temp_word:
        if hand_copy.get(char, 0) == 0:
            return False
        elif hand_copy.get(char, 0) > 0:
            hand_copy[char] -= 1
    
    if temp_word in word_list:
        return True
    return False


def calculate_handlen(hand):
    hand_len = 0
    for value in hand.values():
        hand_len += value
    return hand_len



def play_hand(hand, word_list):
    hand_score = 0
    
    while calculate_handlen(hand) > 0:
        print("Current Hand: ", end= "")
        display_hand(hand)
        word = input("Enter word, or '!!' to indicate that you are finished: ")
        
        if word == '!!':
            print(f"\nTotal score for this hand: {hand_score}")
            print("----------\n")
            return hand_score

        elif is_valid_word(word, hand, word_list):
            word_score = get_word_score(word, calculate_handlen(hand))
            hand_score += word_score
            print(f'"{word}" earned {word_score} points. Total: {hand_score} \n')
        
        else:
            print(f"That is not a valid word. Please choose another word. Total: {hand_score} \n")
        
        hand = update_hand(hand, word)

    print(f"Ran out of letters. Total score: {hand_score} points ")
    print(f"Total score for this hand: {hand_score}")
    print("----------\n")
    return hand_score


def substitute_hand(hand, letter):
    hand_copy = hand.copy()
    if letter in hand.keys():
        number_of_chosen_letter = hand[letter]
        counter = 0
        while counter < number_of_chosen_letter:
            random_letter = random.choice(VOWELS + CONSONANTS)
            if random_letter not in hand:
                random_num = random.randint(1, number_of_chosen_letter - counter)
                hand_copy[random_letter] = random_num
                counter += random_num
        del(hand_copy[letter])
    return hand_copy


def play_game(word_list):
    total_score = 0
    total_hand_num = int(input("Enter total number of hands: "))
    current_hand_num = 0
    is_substitute_used = False
    is_replay_used = False

    while current_hand_num < total_hand_num:
        print(f"HAND {current_hand_num+1} - YOU USE substitute: {is_substitute_used} | replay: {is_replay_used}")
        hand = deal_hand(HAND_SIZE)
        print("Current Hand: ", end= "")
        display_hand(hand)

        if not is_substitute_used:
            substitute_answer = input("\nWould you like to substitute a letter? (yes/no) ").lower()
            if substitute_answer == "yes":
                letter = input("Which letter would you like to replace: ")
                hand = substitute_hand(hand, letter)
                # print("Current Hand: ", end= "")
                # display_hand(hand)
                is_substitute_used = True
            print()
        
        hand_score = play_hand(hand, word_list)
        
        if not is_replay_used:
            answer_to_replay = input("Would you like to replay the hand? (yes/no) ").lower()
            if answer_to_replay == "yes":
                old_hand_score = hand_score
                print()
                new_hand_score = play_hand(hand, word_list)
                hand_score = max(old_hand_score, new_hand_score)
                is_replay_used = True
        
        total_score += hand_score
        current_hand_num += 1

    print("-----END GAME-----")
    print("Total score over all hands:", total_score)
    return total_score


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
