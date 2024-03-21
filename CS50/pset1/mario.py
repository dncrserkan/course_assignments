b = "#"     # brick
s = " "     # space

while True:
    try:
        height = int(input("how many stairs you want? "))
        if 0 < height < 8:
             break
    except ValueError:
        continue


for row in range(height):
        # {space}{bricks}{space}{bricks} + noneed{space}
        print(f"{(height-row-1)*s}{(row+1)*b}{2*s}{(row+1)*b}")
