def main():
    text = input("Input: ")
    new_text = shorten(text)
    print(f"Output: {new_text}")


def shorten(text = ""):
    vovels = "aeiou"
    new_text = ""
        
    for char in text:
        if char.lower() not in vovels:
            new_text += char
    
    return new_text


if __name__ == "__main__":
    main()
