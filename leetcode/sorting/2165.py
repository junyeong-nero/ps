class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            return -int("".join(sorted(str(num)[1:], reverse=True)))
        if num == 0:
            return 0

        counter = Counter(str(num))
        keys = sorted(counter.keys())
        
        res = ""
        if counter["0"] > 0:
            key = keys[1] # next to 0
            counter[key] -= 1
            res = key
        
        for key in keys:
            res += key * counter[key]

        return int(res)
        
