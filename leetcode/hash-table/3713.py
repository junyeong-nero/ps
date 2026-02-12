import collections

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # 1. 모든 가능한 시작점 i를 순회
        for i in range(n):
            counter = collections.defaultdict(int)
            max_freq = 0
            
            # 2. 시작점 i부터 끝점 j까지 늘려가며 확인
            for j in range(i, n):
                char = s[j]
                counter[char] += 1
                
                # 현재 구간에서 가장 많이 등장한 문자의 횟수 갱신
                max_freq = max(max_freq, counter[char])
                
                # 3. 균형 잡힌 구간인지 판별 (핵심 로직)
                # 조건: (구간의 길이) == (고유 문자 개수) * (최대 빈도)
                # 예: "aabb" -> 길이 4 == 문자종류 2개 * 빈도 2 (4 == 4, True)
                # 예: "aabbc" -> 길이 5 == 문자종류 3개 * 빈도 2 (5 != 6, False)
                current_len = j - i + 1
                if max_freq * len(counter) == current_len:
                    ans = max(ans, current_len)
                    
        return ans
