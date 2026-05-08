from typing import List
from collections import defaultdict

class Solution:
    def maxIncreasingCells(self, M: List[List[int]]) -> int:
        m, n = len(M), len(M[0])

        # 같은 값을 가진 셀들을 묶어서 저장
        # A[value] = [[row, col], [row, col], ...]
        A = defaultdict(list)

        for i in range(m):
            for j in range(n):
                A[M[i][j]].append([i, j])

        # dp[i][j]: (i, j) 셀에서 끝나는 최장 증가 경로 길이
        dp = [[0] * n for _ in range(m)]

        # res는 행과 열의 최댓값을 함께 저장하는 배열
        # res[i]는 i번째 행에서 가능한 최장 증가 경로 길이
        # res[~j]는 j번째 열에서 가능한 최장 증가 경로 길이
        #
        # ~j == -j - 1 이므로,
        # res[~0] == res[-1], res[~1] == res[-2] ...
        # 즉, 배열의 뒤쪽을 열 정보 저장용으로 사용
        res = [0] * (m + n)

        # 값을 오름차순으로 처리
        # 현재 값보다 작은 값들만 이전 경로로 사용할 수 있음
        for a in sorted(A):

            # 1단계: 현재 값 a를 가진 모든 셀의 dp 계산
            # 같은 값끼리는 이동할 수 없으므로, 바로 res를 갱신하지 않음
            for i, j in A[a]:
                dp[i][j] = max(res[i], res[~j]) + 1

            # 2단계: 현재 값 a에 대한 dp 계산이 끝난 뒤 res 갱신
            # 이렇게 해야 같은 값끼리 서로 영향을 주지 않음
            for i, j in A[a]:
                res[~j] = max(res[~j], dp[i][j])  # j번째 열 최댓값 갱신
                res[i] = max(res[i], dp[i][j])    # i번째 행 최댓값 갱신

        # 모든 행/열 기준 최장 경로 중 최댓값 반환
        return max(res)
