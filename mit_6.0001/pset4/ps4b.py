import string


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


def get_story_string():
    with open("story.txt", "r") as f:
        story = str(f.read())
    return story


WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text


    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()


    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        puncs = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""  # puncs and space
        dictionary = {}
        for i in range(len(lower)):
            value = (i + shift) % 26
            dictionary[lower[i]] = lower[value]
            dictionary[upper[i]] = upper[value]
        for punc in puncs:
            dictionary[punc] = punc
        return dictionary


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_dict = self.build_shift_dict(shift)
        shifted_message =[]
        for char in self.message_text:
            shifted_message.append(shifted_dict[char])
        return ''.join(shifted_message)



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_list = self.get_valid_words()
        test = []
        big_test = []
        for s in range(26):
            de_text = self.apply_shift(s)
            de_words = de_text.split()
            for word in de_words:
                if is_word(word_list, word):
                    test.append(1)
                else:
                    test.append(0)  # no need but remains for readability
            big_test.append((sum(test), s, de_text))
            del test[:]
        best_shift = max(big_test)  
        # max function will look very first element of every tuples and return whole tuple
        answer = best_shift[1:]
        return answer

if __name__ == '__main__':

    # #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())

    # # Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())

    plaintext_1 = PlaintextMessage('i love you', 6)
    print("Input:", plaintext_1.get_message_text())
    print('Expected Output: o rubk eua')
    print('Actual Output:', plaintext_1.get_message_text_encrypted())
    print("- "*10)

    plaintext_2 = PlaintextMessage('haters gone hate', 2)
    print("Input:", plaintext_2.get_message_text())
    print('Expected Output: jcvgtu iqpc jcvg')
    print('Actual Output:', plaintext_2.get_message_text_encrypted())
    print("- "*10)

    ciphertext_1 = CiphertextMessage('kyzj zj yriu')  # shift = 17
    print("Input:", ciphertext_1.get_message_text())
    print('Expected Output:', (9, 'this is hard'))
    print('Actual Output:', ciphertext_1.decrypt_message())
    print("- "*10)

    ciphertext_2 = CiphertextMessage('kdc wxc rvyxbbrkun')  # shift = 9
    print("Input:", ciphertext_2.get_message_text())
    print('Expected Output:', (17, 'but not impossible'))
    print('Actual Output:', ciphertext_2.decrypt_message())
    print("- "*10)

    story = get_story_string()
    ciphertext_story = CiphertextMessage(story)
    print("story:", ciphertext_story.decrypt_message())
    input()