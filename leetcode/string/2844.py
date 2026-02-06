class Solution:
    def minimumOperations(self, num: str) -> int:
        # delete some digits for divided by 25
        # ends with 00 or 25, 50, 75

        # lists = ["00", "25", "50", "75"]
        n = len(num)
        d = [[] for _ in range(4)]
        for i, c in enumerate(num[::-1]):
            # print(d)
            if c == "0":
                if len(d[0]) == 1:
                    return i - 1
                if len(d[0]) == 0:
                    d[0].append(i)
                if len(d[2]) == 0:
                    d[2].append(i)

            if c == "2":
                if len(d[1]) == 1:
                    return i - 1

            if c == "5":
                if len(d[2]) == 1:
                    return i - 1
                if len(d[1]) == 0:
                    d[1].append(i)
                if len(d[3]) == 0:
                    d[3].append(i)

            if c == "7":
                if len(d[3]) == 1:
                    return i - 1

        return n - num.count("0")

        # lists = ["00", "25", "50", "75"]
        # indices = [num.rfind(s) for s in lists]
        # print(indices)

        # n = len(num)
        # res = n
        # for index in indices:
        #     if index == -1:
        #         continue
        #     res = min(res, n - (index + 2))

        # return res

