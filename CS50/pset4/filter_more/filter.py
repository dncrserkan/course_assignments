import argparse
import struct
import sys
from helpers import BF, BI, RGBTRIPLE, edges, grayscale, blur, reflect


def main():
    # Because of optional arguments are grouped. It is NOT necessary later control groups, only allowed one filter
    parser = argparse.ArgumentParser(description="This program taks a bmp file anr gives a new bmp file according to optional arguments")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("infile", help="Name of input file")
    parser.add_argument("outfile", help ="Name of output file")
    group.add_argument("-b", "--blur", action="store_true", help="blur effect")
    group.add_argument("-g", "--grayscale", action="store_true", help="turn grayscale")
    group.add_argument("-r", "--reflect", action="store_true", help="reflect horizontal")
    group.add_argument("-e", "--edges", action="store_true", help="edges effect")
    args = parser.parse_args()
    
    # Check filter validity - NO NEED
    counter = sum([args.blur, args.grayscale, args.reflect, args.edges]) 
    if counter == 0:
        print("Invalid or missing filter.")
        sys.exit(1)
    if counter > 1:
        print("Only one filter allowed")
        sys.exit(2)

     # Ensure proper useage
    if len(sys.argv) - counter != 3:
        print("Usage: ./filter [flag] infile outfile")
        sys.exit(3)
    
    infile = args.infile
    outfile = args.outfile

    try:
        inptr = open(infile, "rb")
    except FileNotFoundError:
        print("{} file doesn't exist".format(infile))
        sys.exit(4)
    
    try:
        outptr = open(outfile, "wb")
    except:
        print("Could not create {}".format(outfile))
        inptr.close()
        sys.exit(5)
    
    # Read infile's BITMAPFILEHEADER
    bf = struct.unpack("<HIHHI", inptr.read(14))
    # Read infile's BITMAPINFOHEADER
    bi = struct.unpack("<IiiHHIIiiII", inptr.read(40))

    # Set values
    bf = BF(bf[0], bf[1], bf[2], bf[3], bf[4])
    bi = BI(bi[0], bi[1], bi[2], bi[3], bi[4], bi[5], bi[6], bi[7], bi[8], bi[9], bi[10])

    # print_bf(bf)
    # print_bi(bi)

    # Ensure infile is (likely a 24-bit uncompressed BMP 4.0)
    if bf.Type != int(0x4d42) or bf.OffBits != 54 or bi.Size != 40 or bi.BitCount != 24 or bi.Compression != 0:
        inptr.close()
        outptr.close()
        print("Unsupported file format.")
        sys.exit(6)
    
    height = abs(bi.Height)
    width = bi.Width

    # Allocate memory for image
    try:
        image = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(RGBTRIPLE())
            image.append(row)
    except MemoryError:
        print("Not enough memory to allocate image.")
        inptr.close()
        outptr.close()
        sys.exit(7)
    
    # Determine padding for scanlines
    padding = (4 - (width * 3) % 4) % 4     # 3 stands is sizeof(RGBTRIPLE) as bytes

    # Iterate over infile's scanlines
    for i in range(height):
        # Read row into pixel array
        for j in range(width):
            pixel = struct.unpack("<BBB", inptr.read(3))
            image[i][j] = RGBTRIPLE(pixel[0], pixel[1], pixel[2])
        # Skip over padding
        inptr.read(padding)
    
    if args.blur:
        blur(height, width, image)
    elif args.grayscale:
        grayscale(height, width, image)    
    elif args.reflect:
        reflect(height, image)
    elif args.edges:
        edges(height, width, image)


    # Write outfile's BITMAPFILEHEADER
    data = struct.pack("<HIHHI", bf.Type, bf.Size, bf.Reserved1, bf.Reserved2, bf.OffBits)
    outptr.write(data)

    # Write outfile's BITMAPINFOHEARDER
    data = struct.pack("<IiiHHIIiiII", bi.Size, bi.Width, bi.Height, bi.Planes, 
                       bi.BitCount, bi.Compression, bi.SizeImage, bi.XPelsPerMeter, 
                       bi.YPelsPerMeter, bi.ClrUsed, bi.ClrImportant)
    outptr.write(data)

    null_data = struct.pack("<b", 0x00)
    for i in range(height):
        for j in range(width):
            # see_color(i, j, image)
            data = struct.pack("<BBB", image[i][j].blue, image[i][j].green, image[i][j].red)
            outptr.write(data)

        for k in range(padding):
            outptr.write(null_data)
    
    # free memory
    del(image)

    # CLOSE FILES AND EXIT
    inptr.close()
    outptr.close()
    sys.exit(0)


def print_bf(bf):
    """ Sprint bi values """
    print(f"Type: {hex(bf.Type)}")
    print(f"Size: {bf.Size}")
    print(f"Reserved1: {bf.Reserved1}")
    print(f"Reserved2: {bf.Reserved2}")
    print(f"OffBits: {bf.OffBits}")

def print_bi(bi):
    """ print bi values """
    print(f"Size: {bi.Size}")
    print(f"Width: {bi.Width}")
    print(f"Height: {bi.Height}")
    print(f"Planes: {bi.Planes}")
    print(f"BitCount: {bi.BitCount}")
    print(f"Compression: {bi.Compression}")
    print(f"SizeImage: {bi.SizeImage}")
    print(f"XPelsPerMeter: {bi.XPelsPerMeter}")
    print(f"YPelsPerMeter: {bi.YPelsPerMeter}")
    print(f"ClrUsed: {bi.ClrUsed}")
    print(f"ClrImportant: {bi.ClrImportant}")

def see_color(i, j, image):
    """ Image data """
    print(f"b: {image[i][j].blue} \t g: {image[i][j].green} \t r: {image[i][j].red}")



if __name__ == "__main__":
    main()
