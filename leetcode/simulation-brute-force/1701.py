from collections import deque
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # customers = sorted(customers)
        q = deque(customers)
        arr = []

        curr = q[0][0]
        while q:
            
            arrival, time = q.popleft()

            # if not reached to arrival time, move to arrivals.
            if curr < arrival:
                curr = arrival

            curr += time
            wait_time = curr - arrival

            arr.append(wait_time)

        # print(arr)
        return sum(arr) / len(arr)
