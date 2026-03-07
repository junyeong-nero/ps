from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        left = [0] * n
        stack = []

        for i in range(n):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()

            if stack:
                p = stack[-1]
                left[i] = left[p] + maxHeights[i] * (i - p)
            else:
                left[i] = maxHeights[i] * (i + 1)

            stack.append(i)

        right = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()

            if stack:
                p = stack[-1]
                right[i] = right[p] + maxHeights[i] * (p - i)
            else:
                right[i] = maxHeights[i] * (n - i)

            stack.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] - maxHeights[i])

        return ans

# class SegTree:

#     def __init__(self, n):
#         self.n = n
#         self.tree = [0] * (2 * n)

#     def insert(self, pos, value):
#         pos = self.n + pos

#         self.tree[pos] = value
#         while pos:
#             self.tree[pos >> 1] = min(self.tree[pos], self.tree[pos ^ 1])
#             pos >>= 1

#     def query(self, left, right):

#         left += self.n
#         right += self.n

#         res = 0
#         while left <= right:
#             if left % 2 == 1:
#                 res = min(res, self.tree[left])
#                 left += 1
#             if right % 2 == 0:
#                 res = min(res, self.tree[right])
#                 right -= 1
#             left >>= 1
#             right >>= 1

#         return res




# class Solution:
#     def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
#         n = len(maxHeights)

#         tree = SegTree(n)
#         for i in range(n):
#             tree.insert(i, maxHeights[i])

#         ### Segment Tree

#         def func(index):
#             arr = [0] * n
#             arr[index] = maxHeights[index]
#             i = index - 1
#             while i >= 0:
#                 arr[i] = tree.query(i, index - 1)
#                 i -= 1

#             j = index + 1
#             while j < n:
#                 arr[j] = tree.query(index + 1, j)
#                 j += 1
            
#             return sum(arr)

#         res = 0
#         for i in range(n):
#             res = max(res, func(i))

#         return res


        # at index j : left[i] = min(maxHeights[i:j])
        # at index j : right[i] = min(maxHeights[i:j])


        ### prefix sum

        # O(n^2)
        # left[i] = sum of left mountains
        # right[i] = sum of right mountains?
        # stack and pop elem < input
        # [5] -> [3, 3] -> [3, 3, 4] -> [1, 1, 1, 1]
        # [6] -> [5, 5] -> [3, 3, 3] -> 

        # left, right = [0], [0] 

        # stack = deque()
        # value = 0

        # stack_j = deque()
        # value_j = 0

        # for i in range(n):

        #     while stack and stack[-1] > maxHeights[i]:
        #         value -= stack.pop()
        #     count = (i + 1) - len(stack)
        #     stack += deque([maxHeights[i]] * count)
        #     value += maxHeights[i] * count
        #     left.append(value)

        #     j = n - 1 - i
        #     while stack_j and stack_j[-1] > maxHeights[j]:
        #         value_j -= stack_j.pop()
        #     count = (n - 1 - j + 1) - len(stack_j)
        #     stack_j += deque([maxHeights[j]] * count)
        #     value_j += maxHeights[j] * count
        #     right.append(value_j)

        # right = right[::-1]
        # return max([left[i] + right[i] for i in range(n + 1)])

        ### Brute Force

        # 1. 1 <= heights[i] <= maxHeights[i]

        # O(n log n)
        # generate at index i => O(n)
        # index i = max index of maxHeights?

        # def query(index):
        #     heights = [0] * n
        #     heights[index] = max(maxHeights)

        #     i = index - 1
        #     while i >= 0:
        #         heights[i] = min(maxHeights[i], heights[i + 1])
        #         i -= 1
            
        #     j = index + 1
        #     while j < n:
        #         heights[j] = min(maxHeights[j], heights[j - 1])
        #         j += 1
            
        #     return sum(heights)

        # res = 0
        # target = max(maxHeights)
        # for i in range(n):
        #     if maxHeights[i] != target:
        #         continue
        #     res = max(res, query(i))

        # return res

