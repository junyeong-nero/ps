class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # bitmask DP:
        # mask의 i번째 비트가 1이면, 현재까지 선택한 숫자들의 합이 i가 가능하다는 의미
        # 초기에는 아무것도 선택하지 않았으므로 합 0만 가능 → bit 0만 1
        mask = 1

        for row in mat:
            # 다음 상태를 저장할 mask
            mask_next = 0

            # 한 행에서 같은 숫자는 중복 처리할 필요가 없으므로 set으로 변환
            for num in set(row):
                # 현재 가능한 모든 합(mask)에 num을 더한 상태를 생성
                # mask << num : 모든 가능한 합에 num을 더한 효과
                mask_next |= mask << num

            # 다음 행 처리를 위해 mask 갱신
            mask = mask_next

        # target과의 차이를 0부터 점점 늘려가며 확인
        # count()는 0, 1, 2, 3, ... 무한 증가
        for i in count():
            # target - i 가 가능한 합인지 확인
            if (target - i >= 0 and mask & (1 << (target - i)) != 0) or mask & (
                1 << (target + i)
            ) != 0:
                # 가장 먼저 발견되는 i가 최소 차이
                return i


        # d = {0}
        # for row in mat:
        #     d = {x+y for x in d for y in row}
        # return min(abs(target-x) for x in d)

        # m, n = len(mat), len(mat[0])
        # # dp[i] : candidates with mat[:i] rows
        # res = float("inf")

        # @cache
        # def dfs(cur, value=0):
        #     nonlocal res
        #     if cur == m:
        #         if abs(value - target) < abs(res - target):
        #             res = value
        #         return
        #     if value > target + abs(target - res):
        #         return
        #     for num in mat[cur]:
        #         dfs(cur + 1, value + num)

        # dfs(0)
        # return abs(target - res)

        # # dp[i][j]
        # mat = [sorted(row) for row in mat]

        # def get_diffs(arr):
        #     temp = deque()
        #     for i in range(len(arr) - 1):
        #         temp.append(arr[i + 1] - arr[i])
        #     return temp

        # rows = [get_diffs(row) for row in mat]
        # # print(rows)

        # cur = sum([row[0] for row in mat])
        # # print(cur)

        # def get_min_diff(rows):
        #     return min(range(m), key = lambda x: rows[x][0] if rows[x] else float("inf"))

        # res = abs(cur - target)
        # while cur < target:
        #     index = get_min_diff(rows)
        #     if not rows[index]:
        #         break

        #     diff = rows[index].popleft()
        #     cur += diff
        #     res = min(res, abs(cur - target))
        #     print(cur)

        return res

