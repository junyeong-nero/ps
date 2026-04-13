class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        
        def convert(s):
            arr = s.split(":")
            return int(arr[0]) * 60 + int(arr[1])

        t1 = convert(loginTime)
        t2 = convert(logoutTime)

        if (t1 > t2):
            t2 += 60 * 24

        # print(t1, t2)

        t1 = int(ceil(t1 / 15))
        t2 = int(floor(t2 / 15))

        # print(t1, t2)

        return max(0, t2 - t1)
        


