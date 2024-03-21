notepad = {}
while True:
    try:
        item = input().upper()
        if item not in notepad:
            notepad[item] = 1
        else:
            notepad[item] += 1
    
    except EOFError:
        print()
        break

temp = sorted(notepad)
for item in temp:
    print(notepad[item], item)
