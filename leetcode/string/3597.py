class Solution:
    def partitionString(self, s: str) -> List[str]:

        # current sgement has not been seen before
        
        n = len(s)
        segments = []
        seen_segments = set()
        seen_segments.add("")
        
        i = 0

        while i < n:
            
            j = i
            cur = ""
            while j < n and cur in seen_segments:
                cur += s[j]
                j += 1

            # print(cur)
            if cur not in seen_segments:
                seen_segments.add(cur)
                segments.append(cur)

            i = j 

        return segments
            


