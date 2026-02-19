from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum([num for num in nums if num & 1 == 0])
        res = []

        for val, index in queries:
            if val & 1 == 0 and nums[index] & 1 == 0:
                even_sum += val
            if val & 1 and nums[index] & 1 == 0:
                even_sum -= nums[index]
            if val & 1 and nums[index] & 1:
                even_sum += val + nums[index]
            nums[index] += val
            res.append(even_sum)

        return res
            

