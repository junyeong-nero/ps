class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        temp = (1 << n.bit_length()) - 1
        n = n ^ temp
        return n
