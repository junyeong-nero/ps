class Solution:
    def lastInteger(self, n: int) -> int:

        left, rght, step, turn = 1, n, 1, True

        while n > 1: 
            if n % 2 == 0:
                if turn:
                    rght -= step
                else:
                    left += step
            step *= 2
            n = (n + 1) // 2
            turn ^= True

        return left

