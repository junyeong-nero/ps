class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        ### First Solution

        # d = defaultdict(list)
        # d[k] = sum of subsequences ends with k
        # d[k] = [k] + [elem + k for elem in d[k - 1] + d[k + 1]] 
        # [k] : first generated.
        # from d[k - 1] (ends with k - 1)

        # for num in nums:
        #     d[num] += [num] + [elem + num for elem in d[num - 1] + d[num + 1]] 

        # res = sum([sum(value) for value in d.values()]) % MOD
        # return res

        ### Second Solution

        cnt = defaultdict(int)
        total = defaultdict(int)
        
        for num in nums:
            prev_count = cnt[num - 1] + cnt[num + 1]
            prev_sum = total[num - 1] + total[num + 1]
            
            current_count = prev_count + 1            
            current_sum = prev_sum + current_count * num

            cnt[num] = (cnt[num] + current_count) % MOD
            total[num] = (total[num] + current_sum) % MOD
            
        # 모든 가능한 끝자리 숫자에 대한 합을 더함
        return sum(total.values()) % MOD
