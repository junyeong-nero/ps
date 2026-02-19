from collections import deque
from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        arr = []
        for i in range(n - 1):
            temp = 0
            if nums[i] < nums[i + 1]:
                temp = 1
            if nums[i] > nums[i + 1]:
                temp = -1
            
            arr.append(temp)

        def check(arr):
            return all([arr[i] == pattern[i] for i in range(m)])
        
        res = 0
        window = deque(arr[:m])
        # print(window)
        if check(window):
            res += 1

        for i in range(m, n - 1):
            window.popleft()
            window.append(arr[i])

            # print(window)
            if check(window):
                res += 1
        
        return res
