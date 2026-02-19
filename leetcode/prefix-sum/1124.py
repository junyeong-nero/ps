from collections import defaultdict
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        arr = [1 if hour > 8 else -1 for hour in hours]
        prefix = [0]

        for num in arr:
            prefix.append(prefix[-1] + num)

        # print(prefix)
        hist = defaultdict(list)
        res = 0

        for i, num in enumerate(prefix):
            if num >= 1:
                # print(hours[:i])
                res = max(res, i)

            else:
                # find j s.t. i > j and prefix[i] - prefix[j] >= 1 => prefix[i] - 1 >= prefix[j]
                j = i
                for key, value in hist.items():
                    if num - 1 >= key:
                        j = min(j, value[0])
                # print(hours[j:i])
                res = max(res, i - j)

            hist[num].append(i)

        return res
            
