class Solution:
    def minOperations(self, s: str, k: int) -> int:
        """
        문자열 s를 모두 '1'로 만들기 위한 최소 조작 횟수를 구하는 함수
        - 시간 복잡도: O(n) (s.count('0')에서 문자열을 한 번 순회)
        - 공간 복잡도: O(1) (추가적인 배열 생성 없음)
        """
        n = len(s)
        zero_count = s.count('0')  # 문자열 내 '0'의 개수
        
        # 1. 예외 케이스 처리: 문자열 길이(n)와 조작 범위(k)가 같을 때
        if n == k:
            if zero_count == 0:
                # 이미 모두 '1'인 경우, 조작이 필요 없음
                return 0
            elif zero_count == n:
                # 모두 '0'인 경우, 전체를 1번만 뒤집으면 됨
                return 1
            else:
                # '0'과 '1'이 섞여 있으면, 한 번에 모두 '1'로 만들 수 없음
                return -1
        
        # 2. 올림(Ceiling) 연산을 위한 헬퍼 함수
        # math.ceil(x / y)와 동일한 결과를 내는 정수 연산 방식
        # n == k인 경우는 위에서 처리했으므로 y가 0이 되는 ZeroDivisionError는 발생하지 않음
        def ceil_div(x, y):
            return (x + y - 1) // y
        
        # 최소 조작 횟수를 저장할 변수 (초기값은 무한대)
        min_ops = float('inf')
        
        # 3. 조작 횟수가 '짝수(Even)' 번인 경우를 가정
        # 0의 개수(zero_count)가 짝수일 때만 짝수 번의 조작으로 목표 달성 가능
        if zero_count % 2 == 0:
            # 0을 모두 덮기 위한 최소 횟수 계산
            # k개씩 뒤집거나, (n-k) 여분 공간을 활용해 뒤집는 경우 중 최댓값 필요
            m = max(ceil_div(zero_count, k), ceil_div(zero_count, n - k))
            
            # 구한 횟수 m이 홀수라면, 짝수 번 조작을 맞추기 위해 1을 더함
            if m % 2 == 1:
                m += 1
                
            min_ops = min(min_ops, m)
        
        # 4. 조작 횟수가 '홀수(Odd)' 번인 경우를 가정
        # 0의 개수의 홀짝성과 k의 홀짝성이 같을 때만 홀수 번 조작으로 목표 달성 가능
        if zero_count % 2 == k % 2:
            # 홀수 번 조작할 때는 '1'이었던 것들이 결과적으로 뒤집히는 것을 고려
            # (n - zero_count)는 원래 '1'의 개수
            m = max(ceil_div(zero_count, k), ceil_div(n - zero_count, n - k))
            
            # 구한 횟수 m이 짝수라면, 홀수 번 조작을 맞추기 위해 1을 더함
            if m % 2 == 0:
                m += 1
                
            min_ops = min(min_ops, m)
        
        # 5. 결과 반환
        # min_ops가 갱신되었다면 그 값을, 여전히 무한대라면 불가능한 경우이므로 -1 반환
        return int(min_ops) if min_ops < float('inf') else -1

        ### BFS Approach : TLE

#     def minOperations(self, s: str, k: int) -> int:
#         # one operation: k different indices and flips.
#         # 사실 순서는 별로 상관이 없는듯.
#         # 0, 1 의 개수로 처리 가능.?

#         # dp[i] = 1 의 개수가 k 일 떄 최소 operations 횟수
#         # dp[i + k] = dp[i] + 1 / dp[i + 1] + 1 / ... dp[i + k - 1]
#         # 한 번 뒤집을 때 k 개를 뒤집지만, 그중에 0 이 n개 라면 1는 k - n 개. => 결국에 1 은 n 개 만큼 증가하지만, k - n 개 만큼 감소.
#         # 결국 1의 개수는 2n - k 만큼 증가. n 의 범위는 [0, min(k - i, len(s) - i, k)]
#         # 현재 1의 개수가 i 이므로, 0 의 최대 개수는 len(s) - i 이라서.
#         # 뒤집는 1의 개수가 k - n >= i 이여야 하므로, k - i >= n
        
#         n = len(s)
#         start = s.count("1")
#         target = n  # all 1s

#         # 빠른 불가능 판정(선택): k가 짝수면 1의 개수 parity가 보존됨
#         if (k % 2 == 0) and ((start % 2) != (target % 2)):
#             return -1

#         dist = [-1] * (n + 1)
#         dist[start] = 0
#         q = deque([start])

#         while q:
#             curr = q.popleft()
#             if curr == target:
#                 return dist[curr]

#             lo = max(0, k - curr)
#             hi = min(k, n - curr)

#             for i in range(lo, hi + 1):
#                 nxt = curr + 2 * i - k
#                 if dist[nxt] == -1:
#                     dist[nxt] = dist[curr] + 1
#                     q.append(nxt)

#         return -1
