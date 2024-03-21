import sys


def main():
    # Check usage
    if len(sys.argv) != 2:
        print('Usage: ./caesar key')
        sys.exit(1)

    # Check key
    temp = sys.argv[1]
    if temp.isnumeric() and int(temp) > 0:
        key = int(temp)
    else:
        print('Usage: ./caesar key')
        sys.exit(1)

    # Take input
    plain_text = input("PlainText: ")
    clean_text = ""
    encrypted_text = ""
    cipher_text = ""

    # Create a clean version for encryption
    for char in plain_text:
        if char.isascii() and char.isalpha():   # Take ascii letters only
            clean_text += char

    # Change the clean text with encrypted equivalent
    for char in clean_text:
        letter_value = ord(char)
        encrypted_value = letter_value + (key % 26)     # Stay in alphabet in ascii
        if char.isupper() and encrypted_value > 90:
            encrypted_value -= 26
        elif char.islower() and encrypted_value > 122:
            encrypted_value -= 26
        encrypted_text += chr(encrypted_value)

    # Create cipher_text
    encrypted_text = list(encrypted_text)
    for char in plain_text:
        if char.isascii() and char.isalpha():
            cipher_text += encrypted_text.pop(0)
        else:
            cipher_text += char

    print(f"CipherText: {cipher_text}")
    sys.exit(0)



if __name__ == '__main__':
    main()
