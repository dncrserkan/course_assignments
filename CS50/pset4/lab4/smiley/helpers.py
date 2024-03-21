import random


class BF():
    def __init__(self, Type, Size, Reserved1, Reserved2, OffBits):
        self.Type = Type
        self.Size = Size
        self.Reserved1 = Reserved1
        self.Reserved2 = Reserved2
        self.OffBits = OffBits


class BI():
    def __init__(self, Size, Width, Height, Planes, BitCount, 
                 Compression, SizeImage, XPelsPerMeter, YPelsPerMeter, 
                 ClrUsed, ClrImportant):
        self.Size = Size
        self.Width = Width
        self.Height = Height
        self.Planes = Planes
        self.BitCount = BitCount
        self.Compression = Compression
        self.SizeImage = SizeImage
        self.XPelsPerMeter = XPelsPerMeter
        self.YPelsPerMeter = YPelsPerMeter
        self.ClrUsed = ClrUsed
        self.ClrImportant = ClrImportant

    
class RGBTRIPLE():
    def __init__(self, blue = 0, green = 0, red = 0):
        self.blue = blue
        self.green = green
        self.red = red



blue_color = random.randint(0, 255)
green_color = random.randint(0, 255)
red_color = random.randint(0, 255)

def colorize(height, width, image):
    for i in range(height):
        for j in range (width):
            b ,g, r = image[i][j].blue, image[i][j].green, image[i][j].red
            if b == 0 and g  == 0 and r == 0:
                image[i][j].blue = blue_color
                image[i][j].green = green_color
                image[i][j].red = red_color
                # # MORE CREATIVE WAY
                # image[i][j].blue = random.randint(0, 255)
                # image[i][j].green = random.randint(0, 255)
                # image[i][j].red = random.randint(0, 255)
