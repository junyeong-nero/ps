class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # alternating arr

        if len(nums) <= 1:
            return 0
        if len(set(nums)) == 1:
            return len(nums) // 2

        evens = nums[::2]
        odds = nums[1::2]

        even_counter = Counter(evens)
        odd_counter = Counter(odds)

        # print(evens, odds)
        even_info = even_counter.most_common()
        odd_info = odd_counter.most_common()

        # print(even_info, odd_info)

        if even_info[0][0] != odd_info[0][0]:
            return len(evens) - even_info[0][1] + len(odds) - odd_info[0][1]

        res = float("inf")
        if len(odd_info) >= 2:
            res = min(res, len(evens) - even_info[0][1] + len(odds) - odd_info[1][1])
        if len(even_info) >= 2:
            res = min(res, len(evens) - even_info[1][1] + len(odds) - odd_info[0][1])

        return res
