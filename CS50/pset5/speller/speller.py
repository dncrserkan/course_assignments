import sys
import time
import re


words = set()
DICTIONARY = "dictionaries/large"
MAX_LENGHT = 45

word_counter = 0
misspelling_counter = 0

def main():
    # Check usage
    if len(sys.argv) not in [2, 3]:
        print("Usage: speller.py [DICTIONARY] text")
        sys.exit(1)
    
    if len(sys.argv) == 3:
        dictionary = sys.argv[1]
        text = sys.argv[2]
    else:
        dictionary = DICTIONARY
        text = sys.argv[1]
    

    # Load Dictionary
    start = time.time()
    load(dictionary)
    end = time.time()
    time_load = end - start

    # Check Text
    start = time.time()
    check(text)
    end = time.time()
    time_check = end - start

    # Dictionary length
    start = time.time()
    len_words = size()
    end = time.time()
    time_size = end - start

    # Unload
    start = time.time()
    unload()
    end = time.time()
    time_unload = end - start

    time_total = time_load + time_check + time_size + time_unload

    print(f"{'WORDS MISSPELLED:'.ljust(20)} {misspelling_counter}")
    print(f"{'WORDS IN DICTIONARY:'.ljust(20)} {len_words}")
    print(f"{'WORDS IN TEXT:'.ljust(20)} {word_counter}")
    print(f"{'TIME IN load:'.ljust(20)} {time_load:.2f}")
    print(f"{'TIME IN check:'.ljust(20)} {time_check:.2f}")
    print(f"{'TIME IN size:'.ljust(20)} {time_size:.2f}")
    print(f"{'TIME IN unload:'.ljust(20)} {time_unload:.2f}")
    print(f"{'TIME IN total:'.ljust(20)} {time_total:.2f}")


    sys.exit(0)


def load(dictionary):
    try:
        with open(dictionary, "r") as file:
            for line in file:
                words.add(line.rstrip())
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def check(text):

    def open_file(file_name):
        try:
            with open(file_name, "r", encoding='latin-1') as file:
                return file.read()
        except FileNotFoundError:
            print("Text file not found")
            sys.exit(2)
        
    def clean_data(data):
        regex = r"[^0-9a-zA-Z\']"
        return re.sub(regex, " ", data)

    def read_data(data):
        temp = []
        ready = []
        for char in data:
            if not char.isspace():
                temp.append(char)
            else:
                if any(in_char.isnumeric() for in_char in temp):
                    temp = []
                if 0 < len(temp) < MAX_LENGHT:
                    while temp and temp[0] == "'":
                        temp.pop(0)
                    ready.append("".join(temp))
                temp = []
        return ready

    def real_check(text_words):
        print("MISSPELLING WORDS")
        global word_counter
        global misspelling_counter
        word_counter = len(text_words)
        for word in text_words:
            if len(text_words) == 0:
                word_counter -= 1
            elif word.lower() in words:
                continue
            else:
                print(word)
                misspelling_counter += 1
    
    data = open_file(text)
    cleaned_data = clean_data(data)
    text_words = read_data(cleaned_data)
    real_check(text_words)
    

def size():
    return len(words)


def unload():
    global words
    del words


if __name__ == "__main__":
    main()
