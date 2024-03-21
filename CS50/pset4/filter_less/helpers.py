import copy


class BF():
    def __init__(self, Type, Size, Reserved1, Reserved2, OffBits):
        self.Type = Type
        self.Size = Size
        self.Reserved1 = Reserved1
        self.Reserved2 = Reserved2
        self.OffBits = OffBits


class BI():
    def __init__(self, Size, Width, Height, Planes, BitCount, Compression, SizeImage, XPelsPerMeter, YPelsPerMeter, ClrUsed, ClrImportant):
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

    
def grayscale(height, width, image):
    for i in range(height):
        for j in range(width):
            b, g, r = image[i][j].blue, image[i][j].green, image[i][j].red
            temp = (b + g + r) // 3
            image[i][j].blue = temp
            image[i][j].green = temp
            image[i][j].red = temp


def sepia(height, width, image):
    def check_range(value):
        if value > 255:
            return 255
        return value

    for i in range(height):
        for j in range(width):
            b, g, r = image[i][j].blue, image[i][j].green, image[i][j].red
            s_red = int((0.393 * r) + (0.769 * g) + (0.189 * b))
            s_green = int((0.349 * r) + (0.686 * g) + (0.168 * b))
            s_blue = int((0.272 * r) + (0.534 * g) + (0.131 * b))

            image[i][j].blue = check_range(s_blue)
            image[i][j].green = check_range(s_green)
            image[i][j].red = check_range(s_red)


def reflect_hard(height, width, image):
    temp = copy.deepcopy(image)
    for i in range(height):
        for j in range(width):
            pixel = temp[i][j]
            image[i][width - j - 1] = pixel
    del(temp)


def reflect(height, image):
    for i in range(height):
        image[i].reverse()


def blur_hard(height, width, image):
    temp = copy.deepcopy(image)
    for i in range(height):
        for j in range(width):
            if i == 0:
                if j == 0:
                    average_blue = (temp[i][j].blue + temp[i][j+1].blue +temp[i+1][j].blue + temp[i+1][j+1].blue) // 4
                    average_green = (temp[i][j].green + temp[i][j+1].green +temp[i+1][j].green + temp[i+1][j+1].green) // 4
                    average_red = (temp[i][j].red + temp[i][j+1].red +temp[i+1][j].red + temp[i+1][j+1].red) // 4
                elif j == width-1:                    
                    average_blue = (temp[i][j-1].blue + temp[i][j].blue +temp[i+1][j-1].blue + temp[i+1][j].blue) // 4
                    average_green = (temp[i][j-1].green + temp[i][j].green +temp[i+1][j-1].green + temp[i+1][j].green) // 4
                    average_red = (temp[i][j-1].red + temp[i][j].red +temp[i+1][j-1].red + temp[i+1][j].red) // 4
                else:
                    average_blue = (temp[i][j-1].blue + temp[i][j].blue + temp[i][j+1].blue + temp[i+1][j-1].blue + temp[i+1][j].blue + temp[i+1][j+1].blue) // 6
                    average_green = (temp[i][j-1].green + temp[i][j].green + temp[i][j+1].green + temp[i+1][j-1].green + temp[i+1][j].green + temp[i+1][j+1].green) // 6
                    average_red = (temp[i][j-1].red + temp[i][j].red + temp[i][j+1].red + temp[i+1][j-1].red + temp[i+1][j].red + temp[i+1][j+1].red) // 6
            
            elif i == height-1:
                if j == 0:
                    average_blue = (temp[i-1][j].blue + temp[i-1][j+1].blue +temp[i][j].blue + temp[i][j+1].blue) // 4
                    average_green = (temp[i-1][j].green + temp[i-1][j+1].green +temp[i][j].green + temp[i][j+1].green) // 4
                    average_red = (temp[i-1][j].red + temp[i-1][j+1].red +temp[i][j].red + temp[i][j+1].red) // 4
                elif j == width-1:                    
                    average_blue = (temp[i-1][j-1].blue + temp[i-1][j].blue +temp[i][j-1].blue + temp[i][j].blue) // 4
                    average_green = (temp[i-1][j-1].green + temp[i-1][j].green +temp[i][j-1].green + temp[i][j].green) // 4
                    average_red = (temp[i-1][j-1].red + temp[i-1][j].red +temp[i][j-1].red + temp[i][j].red) // 4
                else:
                    average_blue = (temp[i-1][j-1].blue + temp[i-1][j].blue + temp[i-1][j+1].blue + temp[i][j-1].blue + temp[i][j].blue + temp[i][j+1].blue) // 6
                    average_green = (temp[i-1][j-1].green + temp[i-1][j].green + temp[i-1][j+1].green + temp[i][j-1].green + temp[i][j].green + temp[i][j+1].green) // 6
                    average_red = (temp[i-1][j-1].red + temp[i-1][j].red + temp[i-1][j+1].red + temp[i][j-1].red + temp[i][j].red + temp[i][j+1].red) // 6
            
            else:
                if j == 0:
                    average_blue = (temp[i-1][j].blue + temp[i-1][j+1].blue + temp[i][j].blue + temp[i][j+1].blue + temp[i+1][j].blue + temp[i+1][j+1].blue) // 6
                    average_green = (temp[i-1][j].green + temp[i-1][j+1].green + temp[i][j].green + temp[i][j+1].green + temp[i+1][j].green + temp[i+1][j+1].green) // 6
                    average_red = (temp[i-1][j].red + temp[i-1][j+1].red + temp[i][j].red + temp[i][j+1].red + temp[i+1][j].red + temp[i+1][j+1].red) // 6
                elif j == width - 1:
                    average_blue = (temp[i-1][j-1].blue + temp[i-1][j].blue + temp[i][j-1].blue + temp[i][j].blue + temp[i+1][j-1].blue + temp[i+1][j].blue) // 6
                    average_green = (temp[i-1][j-1].green + temp[i-1][j].green + temp[i][j-1].green + temp[i][j].green + temp[i+1][j-1].green + temp[i+1][j].green) // 6
                    average_red = (temp[i-1][j-1].red + temp[i-1][j].red + temp[i][j-1].red + temp[i][j].red + temp[i+1][j-1].red + temp[i+1][j].red) // 6
                else:
                    average_blue = (temp[i-1][j-1].blue + temp[i-1][j].blue + temp[i-1][j+1].blue + temp[i][j-1].blue + temp[i][j].blue + temp[i][j+1].blue + temp[i+1][j-1].blue + temp[i+1][j].blue + temp[i+1][j+1].blue) // 9
                    average_green = (temp[i-1][j-1].green + temp[i-1][j].green + temp[i-1][j+1].green + temp[i][j-1].green + temp[i][j].green + temp[i][j+1].green + temp[i+1][j-1].green + temp[i+1][j].green + temp[i+1][j+1].green) // 9
                    average_red = (temp[i-1][j-1].red + temp[i-1][j].red + temp[i-1][j+1].red + temp[i][j-1].red + temp[i][j].red + temp[i][j+1].red + temp[i+1][j-1].red + temp[i+1][j].red + temp[i+1][j+1].red) // 9
            
            image[i][j].blue = average_blue
            image[i][j].green = average_green
            image[i][j].red = average_red
    del(temp)


def blur(height, width, image):
    temp = copy.deepcopy(image)
    
    for i in range(height):
        for j in range(width):
            divider = 0
            t_blue = 0
            t_green = 0
            t_red = 0

            # loops for kernel
            for k in range(-1,2):
                for l in range(-1, 2):
                    if (i+k) < 0 or (i+k) > (height-1) or (j+l) < 0 or (j+l) > (width-1):
                        # check edges
                        continue

                    # add pixel values for each color
                    t_blue += temp[i+k][j+l].blue
                    t_green += temp[i+k][j+l].green
                    t_red += temp[i+k][j+l].red
                    divider += 1

            image[i][j].blue = t_blue // divider
            image[i][j].green = t_green // divider
            image[i][j].red = t_red // divider
    
    del(temp)
            
            
            
