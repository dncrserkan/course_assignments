from ps4a import get_permutations


def load_words(file_name):
    print("Loading word list from file...")
    with open(file_name, 'r') as inFile:
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        print("  ", len(wordlist), "words loaded.")
        return wordlist


def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


WORDLIST_FILENAME = 'words.txt'

VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
PUNCS = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""  # and space


class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        return self.message_text
    
    def get_valid_words(self):
        return self.valid_words.copy()
    
    def build_transpose_dict(self, vowels_permutation):
        dictionary = {}
        for i, let in enumerate(vowels_permutation.lower()):
            dictionary[VOWELS_LOWER[i]] = let
        for i, let in enumerate(vowels_permutation.upper()):
            dictionary[VOWELS_UPPER[i]] = let
        for let in CONSONANTS_LOWER + CONSONANTS_UPPER + PUNCS:
            dictionary[let] = let
        return dictionary
    
    def apply_transpose(self, transpose_dict):
        enc_message = []
        for let in self.message_text:
            enc_message.append(transpose_dict[let])
        return ''.join(enc_message)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        transpose_dict_list = []
        de_message_list = []
        perm_list = get_permutations('aeiou')
        for perm in perm_list:
            transpose_dict_list.append(self.build_transpose_dict(perm))
        for dic in transpose_dict_list:
            de_message = self.apply_transpose(dic)
            de_message_list.append(de_message)
        test = []
        big_test = []
        word_list = self.get_valid_words()
        for mes in de_message_list:
            de_words = mes.split()
            for word in de_words:
                if is_word(word_list , word):
                    test.append(1)
                else:
                    test.append(0)
            big_test.append((sum(test), mes))
            del test[:]
        best_choice = max(big_test)
        possible_de_message =[]
        
        if best_choice[0] == 0:
            return message3.get_message_text()

        for tup in big_test:
            if tup[0] == best_choice[0] and tup[1] not in possible_de_message:
                possible_de_message.append(tup[1])
        
        de_string = ''
        for mes in possible_de_message:
            de_string = de_string + ', ' + mes
        return de_string[1:]


if __name__ == '__main__':

    # # Example test case
    # message = SubMessage("Hello World!")
    # permutation = "eaiuo"
    # enc_dict = message.build_transpose_dict(permutation)
    # print("Original message:", message.get_message_text(), "Permutation:", permutation)
    # print("Expected encryption:", "Hallu Wurld!")
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    # print("Decrypted message:", enc_message.decrypt_message())
     
    # Test Case 1
    print("\n---START TEST 1---")
    message1 = SubMessage("How are you?")
    permutation1 = "iouae"
    enc_dict1 = message1.build_transpose_dict(permutation1)
    print("Original message:", message1.get_message_text(), "Permutation:", permutation1)
    print("Expected encryption:", "Huw iri yua?")
    print("Actual encryption:", message1.apply_transpose(enc_dict1))
    enc_message1 = EncryptedSubMessage(message1.apply_transpose(enc_dict1))
    print("Decrypted message:", enc_message1.decrypt_message())
    print("---END TEST 1---\n")

    # Test Case 2
    print("\n---START TEST 2---")
    message2 = SubMessage("I made it, i guess")
    permutation2 = "iouae"
    enc_dict2 = message2.build_transpose_dict(permutation2)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation2)
    print("Expected encryption:", "U mido ut, u geoss")
    print("Actual encryption:", message2.apply_transpose(enc_dict2))
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message2.decrypt_message())
    print("---END TEST 2---\n")

    # Test Case 3
    print("\n---START TEST 3---")
    message3 = SubMessage("b brecf ovt, yre truh")
    permutation3 = "iouea"
    enc_dict3 = message3.build_transpose_dict(permutation3)
    print("Original message:", message3.get_message_text(), "Permutation:", permutation3)
    print("Expected encryption:", "b brocf evt, yro trah")
    print("Actual encryption:", message3.apply_transpose(enc_dict3))
    enc_message3 = EncryptedSubMessage(message3.apply_transpose(enc_dict3))
    print("Decrypted message:", enc_message3.decrypt_message())
    print("---END TEST 3---\n")