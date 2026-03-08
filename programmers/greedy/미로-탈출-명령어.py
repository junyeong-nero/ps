def solution(n, m, x, y, r, c, k):
    directions = [
        (1, 0, "d"),
        (0, -1, "l"),
        (0, 1, "r"),
        (-1, 0, "u"),
    ]

    def inbound(a, b):
        return 1 <= a <= n and 1 <= b <= m

    def dist(a, b):
        return abs(r - a) + abs(c - b)

    # 시작부터 불가능한 경우
    start_dist = dist(x, y)
    if start_dist > k or (k - start_dist) % 2 != 0:
        return "impossible"

    answer = []

    for step in range(k):
        remain = k - step - 1

        for dx, dy, ch in directions:
            nx, ny = x + dx, y + dy

            if not inbound(nx, ny):
                continue

            d = dist(nx, ny)

            # 이 칸으로 갔을 때 남은 횟수로 도착 가능해야 함
            if d <= remain and (remain - d) % 2 == 0:
                x, y = nx, ny
                answer.append(ch)
                break

    return "".join(answer) 


# import heapq
# from collections import deque

# def solution(n, m, x, y, r, c, k):
    
#     dirs = [(1, 0), (0, -1), (0, 1), (-1 ,0)]
#     dirs_tags = ["d", "l", "r", "u"]
#     dirs_neg_tags = ["u", "r", "l", "d"]
#     # dlru
    
#     def inbound(a, b):
#         return 1 <= a <= n and 1 <= b <= m
    
#     requires = abs(r - x) + abs(c - y)
#     if requires % 2 != k % 2 or requires > k:
#         return "impossible"
    
#     # 최대한 L, D 를 많이 사용하는게 관건
#     direction = 0
#     res = ""
    
#     while direction < 4:
        
#         dx, dy = dirs[direction]
#         nx, ny = x + dx, y + dy
#         if not inbound(nx, ny):
#             direction += 1
#             continue
#         elif abs(r - nx) + abs(c - ny) <= k - 1:
#             x, y = nx, ny
#             k -= 1
#             res += dirs_tags[direction]
#         else:
#             break
            
#     if k:
#         dx = r - x
#         dy = c - y
#         if dx > 0:
#             res += "d" * abs(dx)
#         if dy < 0:
#             res += "l" * abs(dy)
#         if dy > 0:
#             res += "r" * abs(dy)
#         if dx < 0:
#             res += "u" * abs(dx)
    
#     return res
        
