class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        if n < 2: return 0
        
        # 1. Manacher's Algorithm (홀수 길이 전용)
        # d[i]는 i를 중심으로 하는 팰린드롬의 반지름 (중심 제외 한쪽 길이)
        d = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d[i] = k - 1
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1

        # 2. left[i]: i 위치를 포함하거나 그 이전에 끝나는 최대 팰린드롬 길이
        # right[i]: i 위치를 포함하거나 그 이후에 시작하는 최대 팰린드롬 길이
        left = [1] * n
        right = [1] * n

        # 각 팰린드롬의 '끝점' 기준 최대 길이 기록
        for i in range(n):
            radius = d[i]
            # i+radius 위치에서 끝나는 팰린드롬의 최대 길이는 2*radius + 1
            left[i + radius] = max(left[i + radius], 2 * radius + 1)
            # i-radius 위치에서 시작하는 팰린드롬의 최대 길이는 2*radius + 1
            right[i - radius] = max(right[i - radius], 2 * radius + 1)

        # 3. 빈 공간 채우기 (전파)
        # 왼쪽으로 오면서 팰린드롬 길이는 최대 2씩 줄어들 수 있음 (양 끝을 깎아냄)
        for i in range(n - 2, -1, -1):
            left[i] = max(left[i], left[i + 1] - 2)
        # 누적 최대값 처리 (0..i 범위 내의 최대값)
        for i in range(1, n):
            left[i] = max(left[i], left[i - 1])

        # 오른쪽으로 가면서 동일하게 처리
        for i in range(1, n):
            right[i] = max(right[i], right[i - 1] - 2)
        # 누적 최대값 처리 (i..n-1 범위 내의 최대값)
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i], right[i + 1])

        # 4. 최대 곱 계산
        ans = 1
        for i in range(n - 1):
            # i에서 끝나는 팰린드롬 vs i+1에서 시작하는 팰린드롬
            ans = max(ans, left[i] * right[i + 1])
            
        return ans
