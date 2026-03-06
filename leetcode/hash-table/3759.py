class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        # num is qualified if it has at least k elements in striclty greater than it.

        if k == 0:
            return len(nums)

        counter = Counter(nums)
        keys = sorted(counter.keys())
        
        curr = len(nums)
        res = 0 
        for key in keys:
            curr -= counter[key]
            if curr >= k:
                res += counter[key]

        return res
        

        # keys = sorted(counter.keys())[:-k]
        # return sum([counter[key] for key in keys])
