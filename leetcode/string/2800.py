class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        # trie -> 이거 아님. 순서가 달라질 수 도 있음.
        # overlap 을... naive 하게 해야할 것 같은데.
        # 어짜피 문자열도 3개 밖에 없음. -> 6개 순서
        # abc / acb / bac / bca / cab / cba

        def overlap(x, y):
            if y in x:
                return x

            temp = 0
            for i in range(min(len(x), len(y)) + 1):
                left, right = x[-i:], y[:i]
                if left == right:
                    temp = i
            return x + y[temp:]

        # print(overlap("aba", "aba"))

        res = a + b + c
        for x, y, z in permutations([a, b, c], 3):
            temp = overlap(overlap(x, y), z)
            if len(res) > len(temp):
                res = temp
            elif len(res) == len(temp):
                res = min(res, temp)

        return res
