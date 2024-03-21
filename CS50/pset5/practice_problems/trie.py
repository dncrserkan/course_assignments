import sys


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end


def main():
    # CHECK USAGE
    if len(sys.argv) != 2:
        print("Usage: trie.py infile")
        sys.exit(1)
    
    # OPEN FILE
    try:
        infile = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("Error opening file!")
        return sys.exit(1)

    # CREATE TRIE STRUCTURE
    trie = Trie()
    while True:
        name = infile.readline()
        if name == "":
            break
        trie.insert(name.strip())
    infile.close()

    # SEARCH NAME
    search_for =  input("Check name: ")
    if trie.search(search_for):
        print("Found!")
    else:
        print("Not Found.")
    

    del trie
    sys.exit(0)

    
if __name__ =="__main__":
    main()
