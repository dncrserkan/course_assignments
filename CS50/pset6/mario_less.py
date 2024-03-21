while True:
    try:
        height = int(input("Height: "))
        if 0 < height <= 8:
            break
    except ValueError:
        continue

for i in range(1, height+1):
    print(" " * (height - i) + "#" * i)
