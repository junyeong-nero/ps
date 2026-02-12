class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        
        # 예외 처리: 단어가 적을 때
        if n == 0: return []
        if n == 1: return [0] # 단어가 1개면 제거 후 0개이므로 정의에 따라 처리 (문제 조건 확인 필요)

        # 두 문자열의 LCP 길이 구하는 함수
        def get_lcp_len(s1, s2):
            length = min(len(s1), len(s2))
            count = 0
            for k in range(length):
                if s1[k] == s2[k]:
                    count += 1
                else:
                    break
            return count

        # 1. 인접한 단어들의 LCP 미리 계산 (arr)
        # arr[i]는 words[i]와 words[i+1]의 LCP 길이
        arr = []
        for i in range(n - 1):
            arr.append(get_lcp_len(words[i], words[i+1]))
        
        m = len(arr) # m = n - 1
        
        # 2. Prefix Max (왼쪽부터 누적 최대값)
        prefix = [0] * m
        current_max = 0
        for i in range(m):
            current_max = max(current_max, arr[i])
            prefix[i] = current_max
            
        # 3. Suffix Max (오른쪽부터 누적 최대값)
        suffix = [0] * m
        current_max = 0
        for i in range(m - 1, -1, -1):
            current_max = max(current_max, arr[i])
            suffix[i] = current_max
            
        result = []
        
        for i in range(n):
            # 후보 1: i 제거로 인해 새로 생기는 쌍 (words[i-1] vs words[i+1])
            new_pair_val = 0
            if i > 0 and i < n - 1:
                new_pair_val = get_lcp_len(words[i-1], words[i+1])
            
            # 후보 2: i의 왼쪽 영역 최대값 (arr[0] ... arr[i-2])
            left_max = 0
            if i - 2 >= 0:
                left_max = prefix[i-2]
                
            # 후보 3: i의 오른쪽 영역 최대값 (arr[i+1] ... arr[m-1])
            right_max = 0
            if i + 1 < m:
                right_max = suffix[i+1]
            
            # 세 값 중 최대값이 i를 제거했을 때의 답
            result.append(max(new_pair_val, left_max, right_max))
            
        return result
