import sys

# There are deliberately too many comments

# There must be a comment-line argument
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

# There must be just one comment-line argument
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

# File type must be .py
if file_name[-3:] != ".py":
    sys.exit("Not a Python file")

try:      # This line is a part of actual code
    with open(file_name, "r") as file:
        counter = 0
        for line in file:
            if not (len(line.strip()) == 0 or line.strip()[0] == "#"):
                counter += 1
        print(counter)
except FileNotFoundError:
    sys.exit("File does not exist")

# THIS PROGRAM HAS 17 LINES OF CODES
