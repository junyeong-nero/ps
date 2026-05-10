class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:

        maximumHeight.sort(reverse=True)
        res = height = maximumHeight[0]

        for tower in maximumHeight[1:]:
            height = min(height - 1, tower)
            if height == 0:
                return -1
            res += height

        return res

