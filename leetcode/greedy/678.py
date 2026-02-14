class Solution:
    def checkValidString(self, s: str) -> bool:
        minctr = 0
        maxctr = 0
        for i in s:
            if i == "(":
                minctr += 1
                maxctr += 1
            elif i == ")":
                minctr -= 1
                maxctr -= 1
            else:
                minctr -= 1
                maxctr += 1
            if maxctr < 0:
                return False
            if minctr < 0:
                minctr = 0
        return minctr == 0

