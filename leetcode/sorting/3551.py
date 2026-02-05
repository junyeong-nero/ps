class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(num):
            value = 0
            while num > 0:
                value += num % 10
                num //= 10
            return value

        n = len(nums)
        arr = sorted([(digit_sum(num), num, i) for i, num in enumerate(nums)])

        i = 0
        count = 0
        while i < n:
            j = arr[i][2] 
            if i != j:
                count += 1
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i += 1

        return count

