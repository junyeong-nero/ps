class MagicDictionary:

    def __init__(self):
        self.trie = dict()

    def insert(self, s):
        cur = self.trie
        for c in s:
            if c not in cur:
                cur[c] = dict()
            cur = cur[c]
        cur["."] = s

    def _search(self, trie, s, index=0, wild_card=1):
        if wild_card < 0:
            return False
        if index == len(s):
            return wild_card == 0 and "." in trie
        
        c = s[index]
        for key in trie:
            if key == ".": continue
            if self._search(trie[key], s, index + 1, wild_card - (0 if key == c else 1)):
                return True
    
        return False
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.insert(word)

    def search(self, searchWord: str) -> bool:
        return self._search(self.trie, searchWord, 0, 1)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
