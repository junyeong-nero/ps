class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # 1. 전체 OR 합(S) 구하기 및 비트 매핑
        total_or = 0
        for x in nums:
            total_or |= x
        
        # S에 포함된 비트들만 추려서 인덱스 재부여 (MLE 방지 핵심)
        target_bits = [i for i in range(32) if (total_or >> i) & 1]
        k = len(target_bits)
        bit_map = {bit: i for i, bit in enumerate(target_bits)}
        
        # 2. 매핑된 비트로 숫자들 변환 및 빈도수 측정
        # dp 크기는 2^k (k가 20 이하면 안전)
        dp = [0] * (1 << k)
        for x in nums:
            new_mask = 0
            for i, bit in enumerate(target_bits):
                if (x >> bit) & 1:
                    new_mask |= (1 << i)
            dp[new_mask] += 1
            
        # 3. SOS DP: f[mask] = mask의 부분집합인 원소의 개수
        for i in range(k):
            for mask in range(1 << k):
                if mask & (1 << i):
                    dp[mask] += dp[mask ^ (1 << i)]
        
        # 4. 포함-배제 원리로 OR 합이 정확히 S인 조합 찾기
        # g(S) = sum_{mask subseteq S} (-1)^(k - |mask|) * (2^f(mask))
        total_not_effective = 0
        full_mask = (1 << k) - 1
        
        # 2의 거듭제곱 미리 계산
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        for mask in range(1 << k):
            # 비트 차이 (k - mask의 set bit 수)
            diff = k - bin(mask).count('1')
            term = pow2[dp[mask]] # f(mask)개의 원소로 만들 수 있는 부분집합 수
            
            if diff % 2 == 1:
                total_not_effective = (total_not_effective - term) % MOD
            else:
                total_not_effective = (total_not_effective + term) % MOD
                
        return (pow2[n] - total_not_effective + MOD) % MOD
