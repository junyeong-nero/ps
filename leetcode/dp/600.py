class Solution:
    def findIntegers(self, n: int) -> int:

        # f[i] = length i binary strings without consecutive ones
        f = [0] * 32
        f[0] = 1
        f[1] = 2

        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]

        ans = 0
        prev_bit = 0

        # 높은 비트부터 내려오기
        for i in range(30, -1, -1):
            if n & (1 << i):
                # 현재 비트를 0으로 두고, 아래 i비트를 자유롭게 채우는 경우
                ans += f[i]

                # 이전 비트도 1이면 연속된 1 발생 -> 여기서 종료
                if prev_bit == 1:
                    return ans

                prev_bit = 1
            else:
                prev_bit = 0

        # n 자체도 유효하면 포함
        return ans + 1



        # no consecutive ones.
        # 101010101 
        # 101010

        ### String Based Appoach

        # n 자리 숫자 만들기
        # 1. choose how many a number of ones inserted. let be k >= 1
        # 2. then there are (n - k) zeros. and insert ones between zeros
        # 3. comb(n - k, k - 1)
        # V
        # 10 0 0 0 0 0 
        #   ^ ^   ^ ^ ^

        def func(n):
            if n == 0:
                return 0
            if n == 1:
                return 2

            res = 0
            for k in range(1, n):
                res += comb(n - k, k - 1)
            return res

        arr = [func(i) for i in range(n.bit_length() + 1)]
        prefix = []

        cur = 0
        for num in arr:
            cur += num
            prefix.append(cur)

        print(prefix)
        # prefix[i] : # of i-bits 

        # 0, 1
        # 10
        # 100, 101
        # 1000, 1010, 1001
        # 10000, 10101, 10010, 10001, 10100

        # 100000,
        # 101010, 101001, 100101
        # 101000, 100100 100010, 100001
        
        return prefix[-1]




        ### BFS Approach -> Exploding

        # start with 0
        res = 1

        q = deque([1])
        while q:
            
            cur = q.popleft()
            if cur <= n:
                res += 1 
            else:
                continue

            if cur & 1 == 1:
                q.append(cur << 1)
            if cur & 1 == 0:
                q.append(cur << 1)
                q.append((cur << 1) ^ 1)

        return res
