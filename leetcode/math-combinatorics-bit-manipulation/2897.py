class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:

        # A: 1010 -> 1111
        # B: 0111 -> 0010

        MOD = 10 ** 9 + 7
        # operations 를 할 때 마다 1을 위로 올림.
        # 자리마다 1의 개수를 세면 될 것 같은데?

        d = [0] * 31

        def get_bits(num):
            pos = 0
            while (num >> pos):
                d[pos] += (num >> pos) & 1
                pos += 1
                
        def get_biggest():
            res = 0
            for i in range(31):
                if d[i] > 0:
                    res |= (1 << i)
                    d[i] -=1

            return res

        for num in nums:
            get_bits(num)

        # print(d)

        res = 0
        for _ in range(k):
            t = get_biggest()
            res = (res + t ** 2) % MOD

        # print(d)
        return res


