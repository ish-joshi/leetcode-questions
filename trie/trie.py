
from collections import defaultdict

class Trie:
    
    def __init__(self):
        super().__init__()
        self.root = dict()

        # {a: {b: {}}}
    def insert(self, word: str):
        ref = self.root

        for char in word:

            if ref.get(char) is None:
                ref[char] = {}
            
            ref = ref[char]
        
        ref['$'] = {}
    
    
    def exists(self, word: str) -> bool:
        ref = self.root
        
        for char in word+'$':
            if ref.get(char) is None:
                return False
            ref = ref[char]
        return True

    def __str__(self):
        return str(self.root)


def Test():
    t = Trie()
    t.insert("ishan")
    t.insert("dixita")
    t.insert("didi")
    
    assert t.exists("ishan"), "ishan should exist in the trie"
    assert (not t.exists("ish")), "ish should not exist in trie"

    print ("All cases passed...")

if __name__ == "__main__":
    print("Running Trie Tests...")
    Test()
    
