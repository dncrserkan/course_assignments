import sys
import re


words = set()
DICTIONARY = "dictionaries/large"
MAX_LENGTH = 45

regex = r"[^0-9a-zA-Z\']"
misspelling_counter = 0

def main():
    text = sys.argv[1]

    load(DICTIONARY)
    print(len(words))
    take_words(text)
    print(misspelling_counter)


def load(dictionary):
    with open (dictionary, "r") as file:
        for line in file:
            word = line.rstrip()
            words.add(word)


def take_words(text):
    global misspelling_counter
    tf = open(text, "r")
    whole = tf.read()
    tf.close()
    #print(whole)
    input("Press enter to continue...")
    

    clear_whole = re.sub(regex, " ", whole)     
    #print(clear_whole)
    #print(type(clear_whole))
    input("Press enter to continue...")
    
        
    temp = []
    ready = []
    for char in clear_whole:
        if not char.isspace():
            temp.append(char)

        else:
            for char in temp:
                if char.isnumeric():
                    temp = []
            
            if 0 < len(temp) < MAX_LENGTH:
                #print(temp)
                while len(temp) > 0 and temp[0] == "'":
                    temp.pop(0)
            
                ready.append("".join(temp))
                temp = []
            else:
                temp = []


    
    #print(ready)
    input("Press enter to continue ...")



    test_file = open("test_file.txt", "w")      
    for word in ready:
        if len(word) == 0:
            continue
        if not check(word.lower()):
            val = word + "\n"
            test_file.write(val)
            misspelling_counter += 1
    test_file.close()

def check(word):
    if word in words:
        return True
    return False

if __name__ == '__main__':
    main()
