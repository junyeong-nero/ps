class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        # waviness = # of peaks + valleys
        # design:
        # calculate waviness of num
        # iterate for in [num1, num2]

        # time complexity:
        # calculate waviness -> depends on length of num (e.g. len(100) = 3)
        # therefore, calculate waviness = O(5) constant.
        # then iterate [num1, num2] => O(10^5)
        # it is safe.

        def func(num):
            num = str(num)
            res = 0
            for i in range(1, len(num) - 1):
                a, b, c = num[i - 1], num[i], num[i + 1]
                if a < b > c:
                    res += 1
                if a > b < c:
                    res += 1
            
            return res

        res = 0
        for num in range(num1, num2 + 1):
            res += func(num)

        return res
        
