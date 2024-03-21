while True:
    try:
        height = int(input("Height: "))
        if 0 < height <= 8:
            break
    except ValueError:
        continue

gap = " " * 2
for i in range(1, height+1):
    print((" " * (height-i)) + ("#" * i) + gap + ("#" * i))
