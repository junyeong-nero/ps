class Solution:

    def lis_sequence(self, arr):
        n = len(arr)
        if n == 0:
            return []

        tails = []
        tails_idx = []

        for i, x in enumerate(arr):
            pos = bisect_left(tails, x)

            if pos == len(tails):
                tails.append(x)
                tails_idx.append(i)
            else:
                tails[pos] = x
                tails_idx[pos] = i

        return len(tails)

    def longestSubsequence(self, nums: List[int]) -> int:
        # longest subseq (non-continuous) with non-zero bitwise AND
        # increasing 까지 해야함.

        # A & B = B & A
        # A & B & C ... X > 0 이려면 어떤 조건을 만족해야 하는가?
        # 어떤 index i 에 대해서 A ~ Z 모두 i 번째 bit 가 1 이어야 한다.

        n = len(nums)
        res = 0

        for bit in range(32):

            arr = []
            for num in nums:
                if (num >> bit) & 1:
                    arr.append(num)

            if not arr:
                continue

            res = max(res, self.lis_sequence(arr))

        return res

