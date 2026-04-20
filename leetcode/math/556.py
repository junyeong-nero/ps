from bisect import bisect_right


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # greater -> 어떤 index i < j 를 바꿀 때 s[i] < s[j] 이여야 한다.

        s = list(str(n))
        n = len(s)

        if sorted(s, reverse=True) == s:
            return -1

        # n = 10
        # O(n^2)

        res = float("inf")

        j = n - 1
        while j - 1 >= 0:
            if s[j - 1] < s[j]:
                break
            j -= 1

        arr = sorted(s[j - 1 :])
        i = bisect_right(arr, s[j - 1])

        temp = arr[i]
        arr.pop(i)

        s[j - 1] = temp
        for k in range(j, n):
            s[k] = arr[k - j]

        res = int("".join(s))
        return -1 if res > 2**31 - 1 else res


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i < 0:
            return -1

        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = reversed(nums[i + 1 :])

        res = int("".join(nums))
        return res if res < 2**31 else -1
