class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i = 0
        while True:

            if i >= len(strs[0]):
                return strs[0][:i]

            target = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != target:
                    return strs[0][:i]
            
            i += 1 

        return ""
