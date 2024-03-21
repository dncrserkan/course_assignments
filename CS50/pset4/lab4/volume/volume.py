import sys
import struct


HEADER_SIZE = 44

def main():
    # CHECK USAGE
    if len(sys.argv) != 4:
        print("Usage: ./volume input.wav output.wav factor")
        sys.exit(1)
    
    try:
        infile = open(sys.argv[1], "rb")
    except FileNotFoundError:
        print("File cannot found.")
        sys.exit(1)
    
    try:
        outfile = open(sys.argv[2], "wb")
    except:
        print("File cannot created.")
        sys.exit(1)
    
    try:
        factor = float(sys.argv[3])
    except:
        print("Factor must be number.")
        sys.exit(1)

    # Copy header from input file to output file
    header = struct.unpack(f"<{HEADER_SIZE}b", infile.read(HEADER_SIZE))
    # print("\n", header, "\n")
    outfile.write(struct.pack(f"<{HEADER_SIZE}b", *header))

    # Read samples from input file and write updated data to output file
    while True:
        try:
            sample = struct.unpack("h", infile.read(2))[0]  # unpack returns a tuple
        except:
            print("bytes are finished")
            break
        sample = int(sample * factor)
        outfile.write(struct.pack("h", sample))

    # CLOSE FILES AND EXIT
    infile.close()
    outfile.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
