BITS_IN_BYTE = 8


def print_bulb(bit):
    if bit == 0:
        print("\U000026AB", end="") # Dark emoji
    elif bit == 1:
        print("\U0001F7E1", end="") # Light emoji


def clear_text(text):
    temp_text = ""
    for char in text:
        if char.isascii():     # Check non-english letters
            temp_text += char
    return temp_text


def make_binary(number):
    """ Take a number an returns it's binary equivalent as a string """
    binary_value = ""
    while number >= 1:
        remainder = number % 2
        binary_value = str(remainder) + binary_value
        number = number // 2
    return binary_value



text = input("Message: ")
text = clear_text(text)

text_ascii = [ord(char) for char in text]
text_binary = [make_binary(num) for num in text_ascii]


for row in text_binary:
    # Fix binary input for 8 bit
    while len(row) < BITS_IN_BYTE:
        row = "0" + row

    for bit in row:
        print_bulb(int(bit)) # Print function accepts bit as integer
    print("")
