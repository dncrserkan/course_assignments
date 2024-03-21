import sys
from pyfiglet import Figlet
from random import choice


temp = Figlet()
FONTS = temp.getFonts()

if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid usage")

if len(sys.argv) == 1:
    font = choice(FONTS)

else:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in FONTS:
        sys.exit("Invalid usage")
    
    font = sys.argv[2]


text = input("Input: ")
f = Figlet(font=font)

print("Output:")
print(f.renderText(text))

sys.exit(0)
