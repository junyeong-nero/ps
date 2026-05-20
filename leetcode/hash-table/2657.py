class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        # permutations with length n
        # prefix common array C = 
        # C[i] = # of 

        d = set()
        n = len(A)
        res = 0

        arr = []
        for i in range(n):
            if A[i] in d:
                res += 1
                d.remove(A[i])
            else:
                d.add(A[i])
            
            if B[i] in d:
                res += 1
                d.remove(B[i])
            else:
                d.add(B[i])

            arr.append(res)

        return arr
            

