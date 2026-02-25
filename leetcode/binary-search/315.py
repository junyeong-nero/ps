class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        # O(n log n) 안으로 구현해야함.
        # 무슨 데이터구조를 사용해야 할까...
        # sorted list + binary search?

        # 1 3 5 5 6 7
        #     ^

        n = len(nums)
        arr = []
        res = [0] * n
        for i in range(n - 1, -1, -1):
            num = nums[i]
            j = bisect_left(arr, num)
            res[i] = j
            arr.insert(j, num)

        return res

