class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def helper(startTime, duration, otherStart, otherDuration):
            min_end = float('inf')
            for start, dur in zip(startTime, duration):
                min_end = min(min_end, start + dur)

            res = float('inf')
            for start, dur in zip(otherStart, otherDuration):
                res = min(res, max(min_end, start) + dur)
            return res

        # first evaluate land then water
        # second evaluate water then land
        return min(
            helper(landStartTime, landDuration, waterStartTime, waterDuration),
            helper(waterStartTime, waterDuration, landStartTime, landDuration)
        )
