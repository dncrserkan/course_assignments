import sys
import struct


def main():
    if len(sys.argv) != 3:
        print("Usage: .py infile outfile")
        sys.exit(1)
    
    infile = sys.argv[1]
    outfile = sys.argv[2] 

    try:
        inptr = open(infile, "rb")
    except FileNotFoundError:
        print("Could not open {}".format(infile))
        sys.exit(2)
    
    try:
        outptr = open(outfile, "wb")
    except:
        inptr.close()
        print("Could not create {}".format(outfile))
        sys.exit(3)

    bf = struct.unpack("<HIHHI", inptr.read(14))
    bi = struct.unpack("<IiiHHIIiiII", inptr.read(40))
    bfType = bf[0]
    bfSize = bf[1]
    bfReserved1 = bf[2]
    bfReserved2 = bf[3]
    bfOffBits = bf[4]
    biSize = bi[0]
    biWidth = bi[1]
    biHeight = bi[2]
    biPlanes = bi[3]
    biBitCount = bi[4]
    biCompression = bi[5]
    biSizeImage = bi[6]
    biXPelsPerMeter = bi[7]
    biYPelsPerMeter = bi[8]
    biClrUsed = bi[9]
    biClrImportant = bi[10]
    
    # print(type(bf), bf)
    # print(type(bi), bi)
    # print("")
    # print(type(bfType), bfType)
    # print(type(hex(bfType)), hex(bfType))
    # print(type(0x4d42), int(0x4d42))
    # print(type(bfOffBits), bfOffBits)
    # print(type(biSize), biSize)
    # print(type(biBitCount), biBitCount)
    # print(type(biCompression), biCompression)
    
    if bfType != int(0x4d42) or bfOffBits != 54 or biSize != 40 or biBitCount != 24 or biCompression != 0:
        inptr.close()
        outptr.close()
        print("Unsupported file format.")
        sys.exit(4)


    # Write outfile's BITMAPFILEHEADER
    data = struct.pack("<HIHHI", bfType, bfSize, bfReserved1, bfReserved2, bfOffBits)
    outptr.write(data)

    # Write outfile's BITMAPINFOHEADER
    data = struct.pack("<IiiHHIIiiII", biSize, biWidth, biHeight, 
                       biPlanes, biBitCount, biCompression, biSizeImage, 
                       biXPelsPerMeter, biYPelsPerMeter, biClrUsed, biClrImportant)
    outptr.write(data)

    # Determine padding for scanlines
    padding = (4 - (biWidth * 3) % 4) % 4   # 3 is sizeof(RGBTRIPLE)

    # Iterate over infile's scanlines
    for i in range(abs(biHeight)-1, -1, -1):
        inptr.seek(bfOffBits + (i * ((biWidth * 3) + padding)))
        # Iterate over pixels in scanline
        for _ in range(biWidth):
            rgb = inptr.read(3)
            outptr.write(rgb)
        # outptr.write(inptr.read(biWidth * 3))      # instead of read pixel by pixel

        # Skip over padding, if any       
        inptr.read(padding)

        # Then add it back (to demonstrate how)
        null_data = struct.pack("<b", 0x00)
        for k in range(padding):
            outptr.write(null_data)

    # CLOSE FILES AND EXIT
    inptr.close()
    outptr.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
