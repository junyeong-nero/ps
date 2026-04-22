class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        # 두 번 수정해서 dictionary 와 같은 단어로 만들기.
        # n = 100
        # def check -> O(n)
        # for i -> for i -> O(n^2)
        # total = O(n^3) ~ O(10^6)

        n = len(queries[0])

        def check(src, trg):
            diff = 0
            for i in range(n):
                if src[i] != trg[i]:
                    diff += 1
            return diff

        res = []
        for query in queries:
            for word in dictionary:
                if check(query, word) <= 2:
                    res.append(query)
                    break

        return res
                


