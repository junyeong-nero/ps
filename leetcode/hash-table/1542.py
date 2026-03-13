class Solution:
    def longestAwesome(self, s: str) -> int:
        
        # mask의 k번째 비트:
        # 1 -> 숫자 k의 개수가 홀수
        # 0 -> 숫자 k의 개수가 짝수

        first_seen = {0: -1}  # mask가 처음 등장한 index
        mask = 0
        res = 0

        for i, ch in enumerate(s):
            digit = int(ch)

            # 현재 digit의 홀짝 상태 토글
            mask ^= (1 << digit)

            # 1) 모든 숫자가 짝수인 경우
            if mask in first_seen:
                res = max(res, i - first_seen[mask])
            else:
                first_seen[mask] = i

            # 2) 정확히 한 숫자만 홀수인 경우
            for d in range(10):
                candidate = mask ^ (1 << d)
                if candidate in first_seen:
                    res = max(res, i - first_seen[candidate])

        return res


        # make palindrome
        # maximum length of awesome substring.

        # awesome check
        # freq of each elements, (freq == odd) <= 1

        # def get_odds(counter):
        #     return [key for key in range(10) if counter[key] > 0 and counter[key] % 2 == 1]

        # res = 0

        # # n log n
        # counter = [0] * 10
        # size = 0

        # d = dict()

        # for i, c in enumerate(s):
            
        #     c = int(c)
        #     counter[c] += 1
        #     size += 1

        #     odds = get_odds(counter)
        #     if len(odds) <= 1:
        #         res = max(res, size)
            

        #     j = d.get(tuple(odds), float("inf"))
        #     for k in range(len(odds)):
        #         key = tuple(odds[:k] + odds[k + 1:])
        #         j = min(j, d.get(key, float("inf")))

        #     res = max(res, i - j)
                
        #     if tuple(odds) not in d: 
        #         d[tuple(odds)] = i
            
        #     # at this point. find the appropriate last index j < i
        #     # counter[i] - counter[j] => meets the condition for palindrome
        #     # in O(log n) time complexity

        #     # or check odd numbers info and find it
        #     # [3, 2, 4, 2, 4, 1] -> odds numbers = 3, 1
        #     # check what is last index j s.t. odd numbers only 3 or 1 or both.
        #     # [3] -> only the odds numbers.

        # print(d)
        # return res
