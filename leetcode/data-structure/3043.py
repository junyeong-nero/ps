class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        # longest common prefix between x in arr1, y in arr2
        # check common prefix between x, y
        # it can be solve in O(1)
        #   - convert to str -> compare digit-wise
        
        # but iterate all elements requires n^2
        # n = 5 * 10^4 -> solve in O(n log n)
        # another approach required. trie?

        # build trie with arr1
        # iterate y in arr2, check longest common prefix

        trie = dict()

        def add_trie(s):
            cur = trie
            for c in s:
                if c not in cur:
                    cur[c] = dict()
                cur = cur[c]
            cur["."] = s

        def retrieve(s):
            cur = trie
            res = 0
            for c in s:
                if c not in cur:
                    break
                cur = cur[c]
                res += 1
            
            return res 

        # build trie with arr1
        for x in arr1:
            add_trie(str(x))

        # retrieve with arr2
        res = 0
        for y in arr2:
            res = max(res, retrieve(str(y)))
        
        return res
