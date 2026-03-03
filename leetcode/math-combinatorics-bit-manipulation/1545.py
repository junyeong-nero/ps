class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        mid = 1 << (n - 1)
        if k == mid:
            return "1"
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        mirrored = (1 << n) - k
        bit = self.findKthBit(n - 1, mirrored)
        return "1" if bit == "0" else "0"

# class Solution:
#     def findKthBit(self, n: int, k: int) -> str:
        
#         def invert_and_flip(s):
#             return "".join(["1" if char == "0" else "0" for char in s[::-1]])

#         res = "0"
#         for i in range(n - 1):
#             res = res + "1" + invert_and_flip(res)

#         return res[k - 1]
