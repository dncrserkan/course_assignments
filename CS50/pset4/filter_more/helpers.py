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


def reflect(height, image):
    for line in range(height):
        image[line].reverse()


def blur(height, width, image):
    temp = copy.deepcopy(image)

    for i in range(height):
        for j in range(width):
            divider = 0
            t_blue, t_green, t_red = 0, 0, 0

            # loop for kernel
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (i+k) < 0 or (i+k) > (height-1) or (j+l) < 0 or (j+l) > (width-1):
                        # check corners
                        continue

                    t_blue += temp[i+k][j+l].blue
                    t_green += temp[i+k][j+l].green
                    t_red += temp[i+k][j+l].red
                    divider += 1

            image[i][j].blue = t_blue // divider
            image[i][j].green = t_green // divider
            image[i][j].red = t_red // divider
    
    del(temp)


def edges(height, width, image):
    def check_range(value):
        if value > 255:
            return 255
        return value
    
    # Create temp image and add black edges around it
    temp = []
    for i in range(height+2):
        row = []
        for j in range(width+2):
            row.append(RGBTRIPLE())   # values are innitally zero
        temp.append(row)

    for i in range(1, height+1):
        for j in range(1, width+1):
            temp[i][j].blue = image[i-1][j-1].blue
            temp[i][j].green = image[i-1][j-1].green
            temp[i][j].red = image[i-1][j-1].red

    # Calculate edges
    # define horizontal kernel
    kernel_x = [[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]]
    # define vertical kernel
    kernel_y = [[-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]]
    
    for i in range(1, height+1):
        for j in range(1, width+1):
            gX_b, gX_g, gX_r = 0, 0, 0
            gY_b, gY_g, gY_r = 0, 0, 0

            for k in range(-1, 2):
                for l in range(-1, 2):
                    gX_b += kernel_x[k+1][l+1] * temp[i+k][j+l].blue
                    gX_g += kernel_x[k+1][l+1] * temp[i+k][j+l].green
                    gX_r += kernel_x[k+1][l+1] * temp[i+k][j+l].red

                    gY_b += kernel_y[k+1][l+1] * temp[i+k][j+l].blue
                    gY_g += kernel_y[k+1][l+1] * temp[i+k][j+l].green
                    gY_r += kernel_y[k+1][l+1] * temp[i+k][j+l].red

            g_b = int(((gX_b ** 2) + (gY_b) ** 2) ** (0.5))
            g_g = int(((gX_g ** 2) + (gY_g) ** 2) ** (0.5))
            g_r = int(((gX_r ** 2) + (gY_r) ** 2) ** (0.5))
            
            image[i-1][j-1].blue = check_range(g_b)
            image[i-1][j-1].green = check_range(g_g)
            image[i-1][j-1].red = check_range(g_r)
    del(temp)
