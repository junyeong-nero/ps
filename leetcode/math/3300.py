class Solution:
    def minElement(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            return sum([int(c) for c in str(num)])
        return min(min(nums), min([get_digit_sum(num) for num in nums]))
