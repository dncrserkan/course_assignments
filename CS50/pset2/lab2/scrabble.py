POINTS = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10)


def clear_text(word):
    temp_word = ""
    for i in range(len(word)):
        # Check punctuations, numbers and non-english letters
        if word[i].isascii() and word[i].isalpha():     
            temp_word += word[i]
    temp_word = temp_word.upper()
    return temp_word


def compute_score(word):
    ready_word = clear_text(word)
    score = 0
    for i in range(len(ready_word)):
        letter_order = ord(ready_word[i]) - 65     # start index number from 0
        score += POINTS[letter_order]
    return score


# Get input words from both players
word1 = input("Player 1: ")
word2 = input("Player 2: ")

# Calculate scores for both words
score1 = compute_score(word1)
score2 = compute_score(word2)

# Print the winner
if score1 > score2:
    print("Player 1 wins!")
elif score2 > score1:
    print("Player 2 wins!")
else:
    print("Tie!")
