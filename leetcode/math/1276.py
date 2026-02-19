from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 4x + 2y = tomatoSlices
        # x + y = cheeseSlices
        # 2x = tomatoSlices - 2 cheeseSlices

        # x = (tomatoSlices - 2 cheeseSlices) // 2
        # y = cheeseSlices - x
        temp = tomatoSlices - 2 * cheeseSlices
        if temp < 0 or temp % 2 == 1:
            return []

        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x

        if y < 0:
            return []

        return [x, y]
