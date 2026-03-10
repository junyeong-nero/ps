from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_arr = [1]
        y_arr = [1]

        while x > 1 and x_arr[-1] < bound:
            x_arr.append(x_arr[-1] * x)
        
        while y > 1 and y_arr[-1] < bound:
            y_arr.append(y_arr[-1] * y)

        res = set()
        for x in x_arr:
            for y in y_arr:
                if x + y > bound:
                    continue
                res.add(x + y)

        return sorted(res)
