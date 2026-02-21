class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        max_len = 0
        # dp[prev][curr] stores length of Fibonacci sequence ending at indexes prev, curr
        dp = [[0] * n for _ in range(n)]

        # Map each value to its index for O(1) lookup
        val_to_idx = {num: idx for idx, num in enumerate(arr)}

        # Fill dp array
        for curr in range(n):
            for prev in range(curr):
                # Find if there exists a previous number to form Fibonacci sequence
                diff = arr[curr] - arr[prev]
                prev_idx = val_to_idx.get(diff, -1)

                # Update dp if valid Fibonacci sequence possible
                # diff < arr[prev] ensures strictly increasing sequence
                dp[prev][curr] = (
                    dp[prev_idx][prev] + 1
                    if diff < arr[prev] and prev_idx >= 0
                    else 2
                )
                max_len = max(max_len, dp[prev][curr])

        # Return 0 if no sequence of length > 2 found
        return max_len if max_len > 2 else 0

# class Solution:
#     def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
#         counter = Counter()
#         n = len(arr)
#         res = 0

#         q = deque([(index, [num]) for index, num in enumerate(arr)])
#         while q:
#             index, hist = q.popleft()
#             if res < len(hist) and len(hist) > 2:
#                 # print(hist)
#                 res = len(hist)

#             for i in range(index + 1, n):
#                 if len(hist) <= 1:
#                     q.append((index, hist + [arr[i]]))
#                 elif len(hist) >= 2:
#                     if hist[-1] + hist[-2] != arr[i]:
#                         continue
#                     q.append((index, hist + [arr[i]]))
            
#         return res
