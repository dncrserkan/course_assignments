import emoji


text = input("Input: ")
emojized = emoji.emojize(text, language="alias")
print("Output:", emojized)
