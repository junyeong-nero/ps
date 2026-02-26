class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        step = 0
        while num > 1:
            # print(num)
            if num % 2 == 0:
                num >>= 1
            else:
                num += 1 
            step += 1

        return step
