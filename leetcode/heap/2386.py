class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        maxSum = sum([max(0, num) for num in nums])
        absNums = sorted([abs(num) for num in nums])
        maxHeap = [(-maxSum + absNums[0], 0)]
        ans = [maxSum]
        while len(ans) < k:
            nextSum, i = heapq.heappop(maxHeap)
            heapq.heappush(ans, -nextSum)
            if i + 1 < len(absNums):
                heapq.heappush(maxHeap, (nextSum - absNums[i] + absNums[i + 1], i + 1))
                heapq.heappush(maxHeap, (nextSum + absNums[i + 1], i + 1))
        return ans[0]


# class Solution:
#     def kSum(self, nums: List[int], k: int) -> int:
#         # subsequence
#         # kth largest subseq sum
#         # O(n^2)

#         nums = sorted(nums)
#         # index i 를 가지는 subarray 의 개수는 2 ** (n - 1) 개.
#         # 우리가 없앨 수 있는 방향
#         # top-k 개를 없애고 recursive 하게 수행하기.

#         # [-2, 2, 4] => 4 를 골랐을 때 4 개의 subseq 가 있음
#         # [4], [2, 4], [4, -2], [4, 2, -2] => 일단 이녀석들 제거
#         # [-2, 2] => 에서 k=1 로 다시.

#         prefix = [(float("-inf"), float("inf"))]
#         cur = 0
#         for num in nums:
#             max_value, min_value = prefix[-1]
#             cur += num
#             max_value = max(max_value, cur)
#             min_value = min(min_value, cur)
#             prefix.append((max_value, min_value))

#         print(prefix)

#         def dfs(size, k):
#             print(nums[:size], k)

#             if k == 1:
#                 return prefix[size][0] - prefix[size][1]
#             if k == 2 ** size:
#                 return prefix[size][1]
#             if k > 2 ** (size - 1):
#                 # 일단 현재 largest num 은 안들어감.
#                 return dfs(size - 1, k - 2 ** (size - 1))

#             # 위 조건에 걸리지 않는다는건, 무조건 largest num 이 포함된다는 뜻.
#             return nums[size - 1] + dfs(size - 1, k)

#         res = dfs(len(nums), k)
#         return res

