import re
from collections import deque

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # 연속된 3개 이상의 구슬을 모두 터뜨리는 함수
        def clean(s):
            n = 1
            while n > 0:
                # 동일한 문자가 3번 이상 반복되면 제거 ('\1'은 첫번째 그룹 재참조)
                s, n = re.subn(r'(.)\1{2,}', '', s)
            return s

        # hand의 구슬 순서가 달라도 같은 상태로 취급하기 위해 정렬
        hand = "".join(sorted(hand))
        
        # 큐: (현재 보드 상태, 남은 손패, 사용한 구슬 개수)
        q = deque([(board, hand, 0)])
        # 방문 처리 (무한 루프 방지)
        visited = {(board, hand)}

        while q:
            curr_board, curr_hand, step = q.popleft()

            # 보드를 모두 비웠다면 최소 스텝 반환
            if not curr_board:
                return step

            # 보드의 모든 위치에, 손에 있는 모든 구슬을 넣어보는 완전 탐색
            for i in range(len(curr_board) + 1):
                for j in range(len(curr_hand)):
                    # 중복된 구슬을 같은 자리에 넣는 경우 스킵 (최적화)
                    if j > 0 and curr_hand[j] == curr_hand[j-1]:
                        continue

                    c = curr_hand[j]
                    
                    # [핵심 가지치기(Pruning) 로직]
                    # 아무 곳에나 넣으면 시간초과(TLE)가 발생하므로 의미 있는 곳에만 넣습니다.
                    # 1. 넣으려는 구슬과 같은 색상의 구슬 옆에 놓는 경우
                    # 2. 연속된 같은 색상 구슬 사이에 다른 색상의 구슬을 끼워 넣는 경우 (문제의 테스트 케이스)
                    valid = False
                    if i < len(curr_board) and curr_board[i] == c:
                        valid = True
                    if i > 0 and i < len(curr_board) and curr_board[i-1] == curr_board[i] and curr_board[i] != c:
                        valid = True

                    if valid:
                        # 구슬을 끼워 넣고 연쇄 폭발 처리
                        new_board = clean(curr_board[:i] + c + curr_board[i:])
                        # 사용한 구슬 제거
                        new_hand = curr_hand[:j] + curr_hand[j+1:]
                        
                        if (new_board, new_hand) not in visited:
                            visited.add((new_board, new_hand))
                            q.append((new_board, new_hand, step + 1))

        return -1

# class Solution: 
#     def findMinStep(self, board: str, hand: str) -> int: 
#         n = len(board) 
#         # insert index, usable balls # arr = [("W", 1), ("R", 2)] ... 
#         # insert color ball -> increase color ball at some index 
#         # remove all indices with num >= 3 

#         hand = Counter(hand)
        
#         arr = [] 
#         i = 0
#         while i < n: 
#             j = i
#             while j + 1 < n and board[j] == board[j + 1]:
#                 j += 1 

#             arr.append([board[i], j - i + 1])   
#             i = j + 1 
            
#         def collapse(arr):
#             n = len(arr)
#             changed = False
#             new_arr = []

#             i = 0
#             while i < n:

#                 j = i
#                 temp = arr[j][1]
#                 while j + 1 < n and arr[j][0] == arr[j + 1][0]:
#                     j += 1
#                     temp += arr[j][1]
#                 new_arr.append([arr[i][0], temp])
#                 i = j + 1

#             arr = [elem for elem in new_arr if elem[1] < 3]
#             if len(arr) != n:
#                 return collapse(arr)
#             return arr

#         def query(arr, step = 0):
#             if not arr:
#                 return step

#             # print(arr, step)
#             res = float("inf")
#             for i in range(len(arr)):
#                 ball, count = arr[i]
#                 if 3 - count <= hand[ball]:
#                     hand[ball] -= 3 - count
#                     arr[i][1] = 3

#                     res = min(res, query(collapse(arr), step + 3 - count))

#                     hand[ball] += 3 - count 
#                     arr[i][1] = count

#             return res

#         res = query(arr)
#         return -1 if res == float("inf") else res

