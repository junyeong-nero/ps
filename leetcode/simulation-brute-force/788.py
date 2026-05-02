class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        def rotate(num):

            d = {
                "0": "0",
                "1": "1",
                "8": "8",
                "2": "5",
                "5": "2",
                "6": "9",
                "9": "6",
            }

            res = ""
            for c in num:
                if c not in d:
                    return False
                res += d[c]

            # print(res)
            return res != num

        res = []
        for i in range(1, n + 1):
            if rotate(str(i)):
                res.append(i)

        return len(res)

