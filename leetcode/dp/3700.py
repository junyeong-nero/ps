class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # l, r
        # no equal in adj pairs (a, b)
        # no strictly increasing or striclty decreasing in triplet

        MOD = 10**9 + 7

        # solve in O(n)
        # number of ZigZag arrays

        # [4, 5, 4]
        # 확인해야하는 state 가 2개 있음.
        # 이전 element => 1번 조건을 확인하기 위해서 사용
        # 연속된 2개의 element => 2번 조건을 확인하기 위해서 사용

        # 이거 근데 n 범위가 너무 큰데?
        # 이런식으로는 절대 못품. 수학적으로 접근해야야 될듯?
        # 핵심 아이디어는 이전 pair 에서 증가했다면, 이번에는 감소해야 한다는 거.

        ### Lee's Solution (Transition Metrics)

        # m[i][j] = 1 이면 상태 i -> 상태 j 전이 가능
        # zigzag 조건을 rank 상태로 압축했을 때
        # 전이 가능 조건이 i + j + 1 < k 로 정리됨
        
        import numpy as np

        k = r - l + 1
        m = np.array(
            [[int(i + j + 1 < k) for j in range(k)] for i in range(k)],
            dtype=object
        )

        # 초기 상태:
        # 길이 1에서는 어떤 값에서 시작하든 가능하므로 전부 1
        res = np.ones((1, k), dtype=object)

        # 길이를 1에서 시작했으니, 나머지 n-1번 전이
        n -= 1

        # 빠른 거듭제곱으로 m^(n-1) 계산
        while n:
            if n & 1:
                res = (res @ m) % MOD
            m = (m @ m) % MOD
            n >>= 1

        # 한쪽 패턴만 세었으므로 대칭인 두 패턴을 위해 *2
        return int(res.sum() * 2 % MOD)




        ### Prefix DP

        # 여전히 TLE는 해결을 못함.
        # n 범위가 너무 크다. -> DP 말고 다른 방식을 써야 할 것 같은데 잘 안떠오름.
        # prefix DP 로 바꿔서 어느정도 최적화를 해두긴 했는데. 다른 아이디어가 필요할 것 같다.
        # DP 범위를 최적화 할 수는 있겠지만 근본적인 해결책이 되지는 않을 듯.

        dp = [[0, 0] for _ in range(r + 2)]
        for i in range(l + 1, r + 2):
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = dp[i - 1][1] + 1

        # dp[i][0] : l ~ i - 1 로 끝나고 증가한 녀석들의 개수
        # dp[i][1] : l ~ i - 1 로 끝나고 감소한 녀석들의 개수

        for i in range(n - 1):

            new_dp = [[0, 0] for _ in range(r + 2)]

            for j in range(l, r + 1):
                new_dp[j + 1][0] = (new_dp[j][0] + dp[j][1]) % MOD
                new_dp[j + 1][1] = (new_dp[j][1] + dp[-1][0] - dp[j + 1][0]) % MOD

            dp = new_dp

        return sum(dp[-1]) % MOD



        ### Normal DP

        # dp = [[0, 0] for _ in range(r + 1)]
        # # dp[i][0] = i로 끝나고, 증가한 녀석들의 개수
        # # dp[i][1] = i로 끝나고, 감소한 녀석들의 개수

        # for i in range(l, r + 1):
        #     dp[i][0] = 1
        #     dp[i][1] = 1

        # for i in range(n - 1):

        #     new_dp = [[0, 0] for _ in range(r + 1)]

        #     for j in range(l, r + 1):
        #         new_dp[j][0] = sum([dp[k][1] for k in range(l, j)])
        #         new_dp[j][1] = sum([dp[k][0] for k in range(j + 1, r + 1)])

        #         # dp[k][1] -> prefix[:j]
        #         # dp[k][0] -> prefix[j:]

        #     dp = new_dp
        #     # print(dp)

        # return sum([a + b for a, b in dp])

