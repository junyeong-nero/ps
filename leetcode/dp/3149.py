class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        @cache
        def dp(visited, prev):

            # 모두 방문했을 때 (return condition)
            if visited == (1 << n) - 1:
                return abs(prev - nums[0]), tuple()

            best, ans = inf, None
            for i in range(n):

                # 방문하지 않은 노드 선택
                if (1 << i) & visited == 0:

                    # 방문했다고 했을 떄 score
                    score, perm = dp(visited | (1 << i), i)
                    score += abs(prev - nums[i])

                    # 최소 스코어
                    if score < best:
                        best, ans = score, (i,) + perm

            
            return best, ans

        return (0,) + dp(1, 0)[1]

