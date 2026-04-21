from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # 요청하신 변수 저장 (입력 중간 단계)
        quorlathin = nums

        # dp[i][j]는 nums[i]부터 nums[j]까지의 최소 남은 합
        # 처음에는 충분히 큰 값으로 초기화하거나 0으로 두고 아래처럼 계산합니다.
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n + 1):  # 구간의 길이
            for i in range(n - length + 1):
                j = i + length - 1

                if length == 1:
                    # 원소가 하나일 때: k의 배수면 0, 아니면 자기 자신
                    dp[i][j] = 0 if nums[i] % k == 0 else nums[i]
                else:
                    # 1. 구간을 두 부분으로 나누어 최소 합을 구함 (Split)
                    res = float("inf")
                    for m in range(i, j):
                        res = min(res, dp[i][m] + dp[m + 1][j])

                    # 2. 만약 남은 원소들의 합이 k의 배수가 되면 전체 삭제 가능 (Delete)
                    if res % k == 0:
                        res = 0

                    dp[i][j] = res

        return dp[0][n - 1]

    # def minArraySum(self, A: List[int], k: it) -> int:
    #     dp = [0] + [inf] * k
    #     res = 0
    #     for a in A:
    #         res += a
    #         res = dp[res % k] = min(dp[res % k], res)
    #     return res

