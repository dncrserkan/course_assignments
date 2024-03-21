import sys


class WAVHEADER():
    def __init__(self, chunkID, chunkSize, format, subchunk1ID, subchunk1Size, \
                audioFormat, numChannels, sampleRate, byteRate, blockAlign, \
                bitsPerSample, subchunk2ID, subchunk2Size):
        self.chunkID = chunkID
        self.chunkSize = chunkSize
        self.format = format
        self.subchunk1ID = subchunk1ID
        self.subchunk1Size = subchunk1Size
        self.audioFormat = audioFormat
        self.numChannels = numChannels
        self.sampleRate = sampleRate
        self.byteRate = byteRate
        self.blockAlign = blockAlign
        self.bitsPerSample = bitsPerSample
        self.subchunk2ID = subchunk2ID
        self.subchunk2Size = subchunk2Size


def main():
    # CHECK USAGE
    if len(sys.argv) != 3:
        print("Usage: reverse.py infilename outfilename")
        sys.exit(1)
    
    # Open input file
    try:
        infile = open(sys.argv[1], "rb")
    except FileNotFoundError:
        print(f"{sys.argv[1]} cannot opened")
        sys.exit(1)
    
    # Read data_array from input file
    data = bytearray(infile.read(44))
    header = WAVHEADER(data[0:4], data[4:8], data[8:12], data[12:16], data[16:20], 
                       data[20:22], data[22:24], data[24:28], data[28:32], 
                       data[32:34], data[34:36], data[36:40], data[40:44])
    # print_header(data, header)

    if check_format(header.format):
        try:
            outfile = open(sys.argv[2], "wb")
        except:
            print(f"{sys.argv[2]} cannot opened")
            sys.exit(1)
        
        outfile.write(bytes(data))
        
        sample = bytearray()
        while True:
            buffer = bytearray(infile.read(4))
            if len(buffer) == 0:
                print("END of DATA")
                break
            sample = buffer + sample
        
        outfile.write(bytes(sample))
        infile.close()
        outfile.close()
        sys.exit(0)


def check_format(format_name):
    if format_name == b'WAVE':
        return True
    print(format_name)
    return False


def print_header(data, header):
    print("")
    for i in range(len(data)):
        print(f"{data[i]:02x}", end="\t")
    print("")

    print(  "chunkID: \t", header.chunkID, "\n"
            "chunkSize: \t", header.chunkSize, "\n"
            "format: \t", header.format, "\n"
            "subchunk1ID: \t", header.subchunk1ID, "\n"
            "subchunk1Size: \t", header.subchunk1Size, "\n"
            "audioFormat: \t", header.audioFormat, "\n"
            "numChannels: \t", header.numChannels, "\n"
            "sampleRate: \t", header.sampleRate, "\n"
            "byteRate: \t", header.byteRate, "\n"
            "blockAlign: \t", header.blockAlign, "\n"
            "bitsPerSample: \t", header.bitsPerSample, "\n"
            "subchunk2ID: \t", header.subchunk2ID, "\n"
            "subchunk2Size: \t", header.subchunk2Size, "\n")


if __name__ == "__main__":
    main()
