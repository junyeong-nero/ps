class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        N = len(nums)
        result = [-1] * N
        i = 2 * N - 1

        stack = []
        while i >= 0:
            curr = nums[i % N]

            while stack and stack[-1] <= curr:
                stack.pop()

            if i < N and stack:
                result[i] = stack[-1]

            stack.append(curr)
            i -= 1

        return result

