class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:

        if pattern[0] == pattern[1]:
            temp = text.count(pattern[0]) + 1
            return temp * (temp - 1) // 2
        
        # subsequence 의 개수는 patterns[1] 의 상대적 위치를 확인해야함.
        # acc -> cacc / aacc / accc / acac / acca 이런식으로 됨.
        # a 를 넣을거면 가장 앞에, c 를 넣을거면 가장 뒤에 넣는게 베스트?
        counter = [0, 0]
        res = 0
        for char in text:
            if char == pattern[0]:
                counter[0] += 1
            if char == pattern[1]:
                counter[1] += 1
                res += counter[0]

        # counter[0] 을 더하는 경우 = c 를 마지막에 붙이는 경우
        # counter[1] 을 더하는 경우 = a 를 가장 앞에 붙이는 경우
        res = max(res, res + counter[0], res + counter[1])
        return res

            
