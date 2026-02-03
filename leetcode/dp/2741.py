class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # dp[mask][last_idx]: 사용한 숫자 집합이 mask이고, 마지막 숫자가 nums[last_idx]인 경우의 수
        # 초기화: -1은 아직 방문하지 않음을 의미 (Memoization)
        memo = {}

        def solve(mask, last_idx):
            # 모든 숫자를 다 사용했을 때 (기저 사례)
            if mask == (1 << n) - 1:
                return 1
            
            state = (mask, last_idx)
            if state in memo:
                return memo[state]
            
            count = 0
            for next_idx in range(n):
                # 이미 사용한 숫자인지 확인
                if not (mask & (1 << next_idx)):
                    # 특별한 배열 조건 확인 (나머지가 0인지)
                    if nums[last_idx] % nums[next_idx] == 0 or nums[next_idx] % nums[last_idx] == 0:
                        count = (count + solve(mask | (1 << next_idx), next_idx)) % MOD
            
            memo[state] = count
            return count

        # 처음 시작은 어떤 숫자든 올 수 있으므로 모두 시도
        total_perms = 0
        for i in range(n):
            total_perms = (total_perms + solve(1 << i, i)) % MOD
            
        return total_perms
