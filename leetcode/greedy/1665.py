class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        tasks.sort(key=lambda x: x[0] - x[1])
        res, used = 0, 0

        for actual, minimum in tasks:
            if res - used < minimum:
                res += minimum - (res - used)
            used += actual

        return res
        


