import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: .\license infile")
        sys.exit(1)
    
    file = open(sys.argv[1], "rb")
    buffer = bytearray(file.read(7))
   
    # There is a new line character that we cannot see in the file,
    # Things to try to see the difference
    #   buffer[6] = \n  -> 10   -> new line
    #   buffer[6] = \0  -> 0    -> null
    #   buffer[6] = \t  -> 9    -> tab
    #   buffer[6] = \73 -> I
    
    # more_detail(buffer)
    
    plates = [None] * 8
    idx = 0
    while (len(buffer) == 7):
        buffer[6] = 10
        plates[idx] = buffer
        idx += 1
        buffer = bytearray(file.read(7))

    for i in range(8):
        print(plates[i].decode(), end="")
    
    file.close()



def more_detail(buffer):
    print(type(buffer))
    print(buffer)
    print(len(buffer))
    print()
    for i in range(len(buffer)):
        print(i, "\t", buffer[i], "\t", chr(buffer[i]), "\t", type(buffer[i]))


if __name__ == "__main__":
    main()
