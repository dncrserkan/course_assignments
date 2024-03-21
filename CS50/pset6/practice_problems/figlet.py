from pyfiglet import Figlet
import random
import sys


"""
figlet = Figlet()
figlet.getFonts()               # get available fonts list
figlet.setFont(font = f)        # f is name of font as str
print(figlet.renderText(s))     # s is text as str
"""

figlet = Figlet()
fonts = figlet.getFonts()

def main():
    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)
    
    text = input("Input: ")
    print('Outpu:')
    figlet.setFont(font=font)  
    print(figlet.renderText(text))
    sys.exit(0)


if __name__ == "__main__":
    main()
