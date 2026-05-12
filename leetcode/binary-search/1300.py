class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        n = len(arr)
        arr.sort()

        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        def func(value):
            index = bisect_left(arr, value)
            temp = prefix[index] + (n - index) * value
            return abs(temp - target)

        start, end = 0, arr[-1]
        while start <= end:
            mid = (start + end) // 2
            if func(mid) <= func(mid + 1):
                end = mid - 1
            else:
                start = mid + 1
        
        return start

