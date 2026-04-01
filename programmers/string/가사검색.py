class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        cur.count += 1
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.count += 1

    def search(self, query):
        cur = self.root
        for ch in query:
            if ch == '?':
                return cur.count
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return cur.count


def solution(words, queries):
    tries = {}
    reverse_tries = {}

    for word in words:
        l = len(word)
        if l not in tries:
            tries[l] = Trie()
            reverse_tries[l] = Trie()
        tries[l].insert(word)
        reverse_tries[l].insert(word[::-1])

    answer = []
    for query in queries:
        l = len(query)

        if l not in tries:
            answer.append(0)
            continue

        if query[0] == '?':
            answer.append(reverse_tries[l].search(query[::-1]))
        else:
            answer.append(tries[l].search(query))

    return answer
