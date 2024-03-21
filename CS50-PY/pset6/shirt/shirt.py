from PIL import Image
from os import path
import sys


def main():
    if len(sys.argv) in [1, 2]:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    _, ext1 = path.splitext(sys.argv[1])
    name2, ext2 = path.splitext(sys.argv[2])
    temp = [ext1, ext2]
    for item in temp:
        if item.lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")
    if ext1.lower() != ext2.lower():
        sys.exit("Input and output have different extensions")

    shirt = Image.open("shirt.png")

    try:
        original = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")


    box = create_box(original)
    original = original.crop(box)
    original = original.resize(shirt.size) # resample=Image.LANCZOS

    original.paste(shirt, shirt)
    name = f"{name2}{ext2}"
    original.save(name)
    sys.exit(0)


def create_box(im):
    im_width, im_height = im.size
    top_crop = (im_height - im_width) // 2
    bottom_crop = im_height - top_crop
    return (0, top_crop, im_width, bottom_crop)


if __name__ == "__main__":
    main()
