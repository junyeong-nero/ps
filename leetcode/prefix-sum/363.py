import bisect
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = -10**18

        # 왼쪽 열을 고정
        for left in range(cols):
            # left ~ right 열까지의 행 단위 합을 저장할 1차원 배열
            row_sums = [0] * rows
            
            # 오른쪽 열을 이동
            for right in range(left, cols):
                
                # 1. 두 열 사이의 행 합을 1차원 배열(row_sums)로 누적
                for i in range(rows):
                    row_sums[i] += matrix[i][right]
                
                # 2. 1차원 배열에서 k 이하의 최대 부분배열 합 찾기 (이분 탐색 활용)
                prefix_sums = [0]  # 누적합을 저장할 리스트 (초기값 0)
                curr_sum = 0
                
                for num in row_sums:
                    curr_sum += num
                    
                    # prev_sum >= curr_sum - k 를 만족하는 가장 작은 prev_sum의 인덱스 찾기
                    idx = bisect.bisect_left(prefix_sums, curr_sum - k)
                    
                    # 조건을 만족하는 prev_sum이 존재한다면 최대값 갱신
                    if idx < len(prefix_sums):
                        res = max(res, curr_sum - prefix_sums[idx])
                        
                        # 만약 찾은 값이 k와 정확히 같다면, 더 이상 큰 값을 찾을 수 없으므로 즉시 종료(Early Exit)
                        if res == k:
                            return k
                            
                    # 현재 누적합을 정렬된 위치에 삽입
                    bisect.insort(prefix_sums, curr_sum)
                    
        return res
