import sys


def main():
    if len(sys.argv) != 2:
        print("Usage no-vowel.py word")
        sys.exit(1)

    word = sys.argv[1]
    print(replace(word))
    

def replace(word):
    """ a > 6 | e > 3 | i > 1 | o > 0 | u does not change """
    ref_dict = { "a": "6",
                 "e": "3",
                 "i": "1",
                 "o": "0",
                 # "u": "u"
                }
    temp_list = []
    for char in word:
        if char in ref_dict.keys():
            temp_list.append(ref_dict.get(char))
        else:
            temp_list.append(char)
    
    return "".join(temp_list)


if __name__ == "__main__":
    main()


