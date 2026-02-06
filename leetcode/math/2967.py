class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        nums.sort()
        pal = lambda x: str(x) == str(x)[::-1]
        left = rght = nums[len(nums) // 2] # medium

        while not pal(left):
            left -= 1
        while not pal(rght):
            rght += 1

        return min(
            sum(map(lambda x: abs(x - left), nums)),
            sum(map(lambda x: abs(x - rght), nums)),
        )


# class Solution:
#     def minimumCost(self, nums: List[int]) -> int:
#         # all elements converted to x
#         # cost = sum([abs(elem - x) for elem in nums])
#         # find x s.t. minimize cost

#         # binary search

#         def get_cost(x):
#             return sum([abs(elem - x) for elem in nums])

#         def is_palindrome(num):
#             digits = []
#             while num > 0:
#                 digits.append(num % 10)
#                 num //= 10
#             return digits == digits[::-1]

#         left, right = 0, 10 ** 9
#         while left < right:
#             mid = (left + right) // 2
#             if get_cost(mid) < get_cost(mid + 1):
#                 right = mid
#             else:
#                 left = mid + 1

#         if is_palindrome(left):
#             return get_cost(left)

#         return 0

