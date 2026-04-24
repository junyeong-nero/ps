class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:

        # solve within log n
        # 범위 내에 하나하나 체크하는 방식으로 가면 안될 것 같다.
        # 반대로 생성하는 방향으로 가야함. 그게 더 시간복잡도가 적을 것 같음.
        # 처음 [(1, 1, 1), (2, 2), 3, 4 ... 9] 이렇게 해두고 (cur, prod, sum)
        # 여기에다가 0-9 숫자를 더하면 2자리 수가 된다. 그러면 cur * 10 + k, prod * k, sum + k 가 되고
        # cur * 10 + k 범위가 r 을 넘어가면 삭제. r 보다 같거나작은 경우, l 보다 작은 경우로 나눠서 저장

        # DP

        def func(num):
            if num == 0:
                return 0

            arr = [int(c) for c in str(num)]

            @cache
            def dfs(index, total=0, prod=1, check=False):
                if index == len(arr):
                    return total and prod % total == 0

                res = 0
                bound = 10 if check else (arr[index] + 1)
                for k in range(bound):
                    temp = k < arr[index]
                    res += dfs(
                        index + 1,
                        total + k,
                        prod * (k if total > 0 or (total == 0 and k > 0) else 1),
                        check | temp,
                    )

                return res

            return dfs(0)

        L = func(l - 1)
        R = func(r)
        # print(L, R)

        return R - L









        # BFS -> 이것도 exploding 함

        q = deque()
        for i in range(1, 10):
            q.append((i, i, i))

        count = 0

        while q:

            for _ in range(len(q)):
                cur, prod, total = q.popleft()
                if prod % total == 0:
                    if l <= cur <= r:
                        count += 1

                for k in range(10):
                    if cur * 10 + k > r:
                        continue
                    # pruninig at k == 0?
                    q.append((cur * 10 + k, prod * k, total + k))

        return count

        # def check(k):
        #     prod, total = 1, 0
        #     for c in str(k):
        #         prod *= int(c)
        #         total += int(c)
        #     return prod % total == 0

        # for i in range(1, 1000):
        #     print(i, check(i))

        return 0

