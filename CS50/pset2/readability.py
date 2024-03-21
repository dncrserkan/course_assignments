text = input("Text: ")

letter = 0
sentence = 0
word = 1    # Last word has no space, so we start by counting it 

for char in text:
    if char.isalpha():
        letter += 1
    elif char == " ":
        word += 1
    elif char in ["!", "?", "."]:
        sentence += 1

L = 100 * letter / word
S = 100 * sentence / word
index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print(f"Before Grade: 1")
elif index >= 16:
    print(f"Grade: 16+")
else:
    print(f"Grade: {index}")
