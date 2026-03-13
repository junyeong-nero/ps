class Solution:
    def minNumberOfSeconds(self, h: int, times: List[int]) -> int:
        
        n = len(times)
        prefix = [0]
        cur = 1
        for i in range(h):
            prefix.append(prefix[-1] + cur)
            cur += 1
        # print(prefix)

        ### Binary Search

        def can(target_time: int) -> bool:
            res = 0
            for t in times:
                k = bisect_right(prefix, target_time // t) - 1
                res += k
                if res >= h:
                    return True
            return False

        left, right = 0, min(times) * prefix[-1]

        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1

        return left

        ### BFS
        # q = [(0, 0, 0)]

        # d = [float("inf")] * (h + 1)
        # d[0] = 0

        # while q:
            
        #     dist, height, index = heappop(q)
        #     if index == n:
        #         continue

        #     for dh, mul in enumerate(prefix):

        #         new_dist = max(dist, times[index] * mul)
        #         new_height = height + dh

        #         if new_height <= h and new_dist < d[new_height]:
        #             d[new_height] = new_dist
        #             heappush(q, (new_dist, new_height, index + 1))
            
        
        # print(d)
        # return d[-1]
