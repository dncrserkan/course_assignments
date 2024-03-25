import sys


def main():
    # CHECK USAGE
    if len(sys.argv) != 2:
        print("Usage: recovery.py file_name")
        sys.exit(1)
    
    # Open input file
    try:
        infile = open(sys.argv[1], "rb")
    except:
        print("File could not be opened.")
        sys.exit(1)

    
    FAT_LONG = 512
    is_file_writing = False     # Flag indicating whether the file is in process
    name_counter = 0
    possible_fourths = [0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, \
                        0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, 0xef]

    while True:
        # Read first block
        try:
            data = infile.read(FAT_LONG)
            buffer = bytearray(data)
        except:
            sys.exit(99)

        # if buffer:
        #     print(buffer[0], "\t", buffer[1], "\t", buffer[2], "\t", buffer[3])

        if not is_file_writing:
            # Check if data is ended
            if len(buffer) == 0:
                print("END of DATA")
                sys.exit(0)
            
            # Check first 3 bytes are suitable for JPG then the fourth byte
            if buffer.startswith(b'\xff\xd8\xff') and buffer[3] in possible_fourths:
                # Arrange name of output and open new file
                name_outfile = f'{name_counter:03}.jpg'
                name_counter += 1
                try:
                    outfile = open(name_outfile, "wb")
                    is_file_writing = True # File is in writing process now
                except:
                    print(f"{name_outfile} file could not be opened")
                    sys.exit(1)
                
                # Write data block in outfile
                outfile.write(data)

        else:
            # Check if data is ended
            if len(buffer) == 0:
                print("END of DATA")
                sys.exit(0)
            # Check if it is a new JPG
            if buffer.startswith(b'\xff\xd8\xff') and buffer[3] in possible_fourths:
                # New bytes indicate a new jpg
                # Close last file
                outfile.close()

                # Arange name of output and open new file
                name_outfile = f'{name_counter:03}.jpg'
                name_counter += 1
                try:
                    outfile = open(name_outfile, "wb")
                    is_file_writing = True # New file is in writing process now
                except:
                    print(f"{name_outfile} file could not be opened")
                    sys.exit(1)
                
                # Write data block in outfile
                outfile.write(data)
            
            else:
                # Keep writing data block in outfile
                outfile.write(data)


if __name__ == "__main__":
    main()
