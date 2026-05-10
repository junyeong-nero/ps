class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # total duration is divisible by 60

        # design:
        # - d[p] = list of indices with time % 60 == p
        # - find d[60 - time[i]] for i in range(n)
        #   - do bisect left to find range of j

        # time complexity:
        # n = 6 * 10^4 -> solve in O(n log n)
        # construct d[p] : O(n)

        
        n = len(time)
        d = [0] * 61

        res = 0
        for i, t in enumerate(time):
            res += d[60 - t % 60]
            d[t % 60] += 1

        res += d[0] * (d[0] - 1) // 2

        return res

        
