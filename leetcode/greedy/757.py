class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        ### Greedy Approach with last index
        
        # 1) end 오름차순
        # 2) end가 같으면 start 내림차순
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # 지금까지 선택한 점들 중 가장 큰 두 점
        # p1 < p2 형태로 유지
        p1 = -1
        p2 = -1

        ans = 0

        for l, r in intervals:
            # 현재 interval [l, r] 안에 선택된 점이 0개인 경우
            if l > p2:
                ans += 2
                p1, p2 = r - 1, r

            # 현재 interval [l, r] 안에 선택된 점이 1개인 경우
            elif l > p1:
                ans += 1
                p1, p2 = p2, r

            # 이미 2개 이상 포함된 경우
            else:
                continue

        return ans


        ### Prefix + Greedy Approach
        # - Greedy is not optimal solution for prefix
        # TC failed at 90/118

        # containing set : at least two integers in nums
        # minimum possible size

        # prefix. -> overlaped indices first
        
        n = len(intervals)
        hist_add = defaultdict(set)
        hist_remove = defaultdict(set)

        for i, (a, b) in enumerate(intervals):
            hist_add[a].add(i)
            hist_remove[b].add(i)

        # choose maximum prefix points 
        cur = set()
        prefix = dict()

        # O(N)
        for point in sorted(hist_add.keys() | hist_remove.keys()):
            if point in hist_add:
                cur = cur | hist_add[point]

            prefix[point] = cur

            if point in hist_remove:
                cur = cur - hist_remove[point]

        print(prefix)

        # concatenate prefix.
        counter = {i:0 for i in range(n)}
        used = set()

        ### 이부분 다르게 풀 수는 없나?

        # 일단 문제가 잇는게, index 를 여러번 쓸 수 있음.
        # 어렵네. 잘 모르겠다. greedy 방식말고는 잘 안떠오름
        # 

        # O(N)
        def choose():
            left = {key for key, value in counter.items() if value < 2}
            max_intersect = 0
            max_prefix = -1

            for i in prefix:
                if i in used: continue
                if len(prefix[i] & left) > max_intersect:
                    max_intersect = len(prefix[i] & left)
                    max_prefix = i
            
            return max_prefix, len(left)

        res = float("inf")
        temp = 0

        # O(N^2)
        while True:
            i, k = choose()
            if i == -1:
                break
            used.add(i)
            for point in prefix[i]:
                counter[point] += 1

            print(i, counter)
            temp += 1

        res = min(res, temp)
        return res
