import sys
import string


ALPHABET = string.ascii_uppercase


def main():
     # Check usage
    if len(sys.argv) != 2:
        print('Usage: ./substitution SECRETKEY')
        sys.exit(1)

    # Check key
    key = sys.argv[1].upper()
    
    if len(key) != 26:
        print("Key must contain 26 charcaters.")
        sys.exit(1)
    
    unique_test = ""
    for char in key:
        if char.isascii() and char.isalpha() and char not in unique_test:
            unique_test += char
    
    if len(unique_test) != 26:
        print("Key must contain 26 unique charcaters.")
        sys.exit(1)
    
    # Take and encrypt input
    plain_text = input("PlainText:\t")
    cipher_text = ""

    for char in plain_text:
        try:
            position = ALPHABET.index(char.upper())
            if char.isupper():
                cipher_text += key[position]
            else:
                cipher_text += key[position].lower()
        except ValueError:
            cipher_text += char

    print(f"CipherText: \t{cipher_text}")

if __name__ == '__main__':
    main()
