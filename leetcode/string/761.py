class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        # must start with 1 (every prefix has # of 1 > # of 0)
        # 110101

        def func(s):

            def check(i):
                prefix_counter = 1 if s[i] == "1" else -1
                arr = []
                j = i + 1
                while prefix_counter > 0 and j < n:
                    prefix_counter += 1 if s[j] == "1" else -1
                    j += 1
                return (i, j) if prefix_counter == 0 else None

            n = len(s)
            d = dict()
            for i in range(n):
                temp = check(i)
                if not temp:
                    continue
                d[temp[0]] = temp[1]

            def swap(s, i):
                arr = []
                cur = i
                while cur in d:
                    prev = cur
                    cur = d[cur]
                    arr.append(s[prev:cur])

                if len(arr) <= 1:
                    return s

                # print(arr)
                arr = sorted(arr, reverse=True)
                return s[:i] + "".join(arr) + s[cur:]

            res = []
            for i in range(n):
                res.append(swap(s, i))

            return res

        q = deque([s])
        visited = set()
        res = s

        while q:
            tar = q.popleft()
            if tar in visited:
                continue
            visited.add(tar)
            res = max(res, tar)

            cand = func(tar)
            for s in cand:
                if s in visited:
                    continue
                q.append(s)

        return res

        # n = len(s)
        # arr = []
        # for i in range(n):
        #     temp = check(i)
        #     if temp:
        #         arr.append(temp)

        # def swap(s, a, b):
        #     return s[: a[0]] + s[b[0] : b[1]] + s[a[0] : a[1]] + s[b[1] :]

        # res = s
        # m = len(arr)
        # for i in range(m):
        #     for j in range(i + 1, m):
        #         if arr[i][1] != arr[j][0]:
        #             continue
        #         print(arr[i], arr[j])

        #         temp = swap(s, arr[i], arr[j])
        #         res = max(res, temp)

        # return res

