from typing import List, Tuple

class Solution:
    def get_decreasing_segments(self, nums: List[int]) -> List[Tuple[int, int, int]]:
        """
        배열을 순회하며 '연속된 감소 구간'들을 찾아 리스트로 반환합니다.
        반환값: (시작 인덱스, 끝 인덱스, 해당 구간의 합)의 리스트
        """
        n = len(nums)
        segments = []

        start_idx = 0
        current_sum = nums[0]

        for i in range(1, n):
            # 감소 조건이 깨지는 경우 (즉, 증가하거나 같아진 경우)
            # 지금까지의 감소 구간을 저장하고 새로 시작합니다.
            if nums[i - 1] <= nums[i]:
                segments.append((start_idx, i - 1, current_sum))
                start_idx = i
                current_sum = 0
            
            current_sum += nums[i]

        # 마지막 남은 구간 처리
        segments.append((start_idx, n - 1, current_sum))
        return segments

    def maxSumTrionic(self, nums: List[int]) -> int:
        """
        Trionic 수열(증가 -> 감소 -> 증가)의 최대 합을 구합니다.
        전략:
        1. 왼쪽에서 오른쪽으로 '증가하는 부분 수열'의 최대 합을 미리 계산 (DP)
        2. 오른쪽에서 왼쪽으로 '증가하는 부분 수열'의 최대 합을 미리 계산 (DP)
        3. 모든 '감소 구간'을 순회하며, 해당 구간의 왼쪽과 오른쪽에 
           미리 구해둔 증가 구간을 붙여 최댓값을 갱신.
        """
        n = len(nums)
        if n < 3:
            return 0 # 혹은 문제 조건에 맞는 최소값

        # ---------------------------------------------------------
        # 1. 왼쪽 증가 구간 전처리 (Left Increasing DP)
        # max_inc_ending_at[i]: 인덱스 i에서 끝나는 연속 증가 수열의 최대 합
        # ---------------------------------------------------------
        max_inc_ending_at = [0] * n
        for i in range(n):
            max_inc_ending_at[i] = nums[i]
            # 이전 값보다 크다면(증가), 이전까지의 합과 연결 시도
            if i > 0 and nums[i - 1] < nums[i]:
                # 카데인 알고리즘: 이전 합이 양수일 때만 더하는 것이 이득
                if max_inc_ending_at[i - 1] > 0:
                    max_inc_ending_at[i] += max_inc_ending_at[i - 1]

        # ---------------------------------------------------------
        # 2. 오른쪽 증가 구간 전처리 (Right Increasing DP)
        # max_inc_starting_at[i]: 인덱스 i에서 시작하는 연속 증가 수열의 최대 합
        # (역방향으로 순회하며 계산)
        # ---------------------------------------------------------
        max_inc_starting_at = [0] * n
        for i in range(n - 1, -1, -1):
            max_inc_starting_at[i] = nums[i]
            # 다음 값보다 작다면(오른쪽으로 갈수록 증가), 다음 구간과 연결 시도
            if i < n - 1 and nums[i] < nums[i + 1]:
                if max_inc_starting_at[i + 1] > 0:
                    max_inc_starting_at[i] += max_inc_starting_at[i + 1]

        # ---------------------------------------------------------
        # 3. 감소 구간을 중심으로 결합 (Combine)
        # ---------------------------------------------------------
        # 모든 연속된 감소 구간 추출
        decreasing_segments = self.get_decreasing_segments(nums)
        
        ans = float('-inf')

        for start, end, seg_sum in decreasing_segments:
            # 유효한 Trionic 구조가 되기 위한 조건 확인:
            # 1. 감소 구간의 왼쪽(start-1)이 존재하고, Peak를 형성해야 함 (nums[start-1] < nums[start])
            # 2. 감소 구간의 오른쪽(end+1)이 존재하고, Valley를 형성해야 함 (nums[end] < nums[end+1])
            # 3. 감소 구간의 길이가 최소 2 이상이어야 함 (start < end)
            if (start > 0 and nums[start - 1] < nums[start] and
                end < n - 1 and nums[end] < nums[end + 1] and
                start < end):
                
                # 왼쪽 최대 증가 합 + 현재 감소 구간 합 + 오른쪽 최대 증가 합
                current_trionic_sum = max_inc_ending_at[start - 1] + seg_sum + max_inc_starting_at[end + 1]
                
                if current_trionic_sum > ans:
                    ans = current_trionic_sum

        return ans if ans != float('-inf') else 0


    
# class Solution:
#     def maxSumTrionic(self, nums: List[int]) -> int:

#         n = len(nums)
#         # increase bound, decrease bound

#         prefix = [0]
#         for num in nums:
#             prefix.append(prefix[-1] + num)

#         increase = []
#         decrease = []

#         i = 0
#         while i < n:
#             j = i
#             min_prefix, min_index = float("inf"), None
#             max_prefix, max_index = float("-inf"), None
#             while j + 1 < n and nums[j] < nums[j + 1]:
#                 j += 1

#             # print(i, j)
#             for p in range(i, j):
#                 if prefix[p] < min_prefix:
#                     min_prefix = prefix[p]
#                     min_index = p
#                 if prefix[p + 2] > max_prefix:
#                     max_prefix = prefix[p + 2]
#                     max_index = p + 1
            
#             if max_index and i < max_index:
#                 increase.append((i, max_index))
#             if min_index and min_index < j:
#                 increase.append((min_index, j))
#             i = j + 1
        
#         i = 0
#         while i < n:
#             j = i
#             while j + 1 < n and nums[j] > nums[j + 1]:
#                 j += 1
#                 if i < j:
#                     decrease.append((i, j))            
#             i = j + 1

#         print("increase", increase)
#         print("decrease", decrease)

#         # increase -> decrease -> increase

#         @cache
#         def dfs(start, end, section=0):
#             res = float("-inf")
#             if section == 0:
#                 for a, b in increase:
#                     res = max(res, dfs(a, b, section=1))
#             elif section == 1:
#                 for a, b in decrease:
#                     if a != end:
#                         continue
#                     res = max(res, dfs(start, b, section=2))
#             elif section == 2:
#                 for a, b in increase:
#                     if a != end:
#                         continue
#                     res = max(res, dfs(start, b, section=3))
#             elif section == 3:
#                 return prefix[end + 1] - prefix[start]

#             return res

#         res = dfs(0, 0)
#         return res




