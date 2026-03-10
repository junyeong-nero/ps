def solution(numbers):
    positions = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1)
    }
    
    
    def get_cost(a, b):
        if a == b:
            return 1
        xa, ya = positions[a]
        xb, yb = positions[b]
        
        dx, dy = abs(xa - xb), abs(ya - yb)
        p, q = min(dx, dy), max(dx, dy)
        return  2 * (q - p) + 3 * p
    
    
    # dp[i][l][r] : i번째 버튼을 누를 때, 오른손이 r, 왼손이 l 위치에 있을 때의 소요 시간?
    
#     q = deque([(0, 4, 6)])
#     map = dict()
    
#     for index in range(n):
        
#         number = int(numbers[index])
        
#         for _ in range(len(q)):
#             cost, left, right = q.popleft()
#             q.append((cost + get_cost(left, number), number, right))
#             q.append((cost + get_cost(right, number), left, number))
                     
#     # print(q)
#     return min([cost for cost, _, _ in q])
    
    ### DP
#     dp = [[[float("inf") for _ in range(10)] for _ in range(10)] for _ in range(n + 1)]
#     dp[0][4][6] = 0
    
#     for i in range(1, n + 1):
#         cur = int(numbers[i - 1])
#         for r in range(10):
#             for l in range(10):
#                 dp[i][cur][l] = min(dp[i][cur][l], dp[i - 1][r][l] + cost(r, cur))
#                 dp[i][r][cur] = min(dp[i][r][cur], dp[i - 1][r][l] + cost(l, cur))
    
    
#     res = float("inf")
#     for r in range(10):
#         for l in range(10):
#             res = min(res, dp[-1][r][l])

    # (left, right) -> min_cost
    dp = {(4, 6): 0}

    for ch in numbers:
        num = int(ch)
        next_dp = {}

        for (left, right), cost in dp.items():
            # 왼손으로 누르기
            if num != right:
                new_cost = cost + get_cost(left, num)
                state = (num, right)
                if state not in next_dp or next_dp[state] > new_cost:
                    next_dp[state] = new_cost

            # 오른손으로 누르기
            if num != left:
                new_cost = cost + get_cost(right, num)
                state = (left, num)
                if state not in next_dp or next_dp[state] > new_cost:
                    next_dp[state] = new_cost

        dp = next_dp

    res = min(dp.values())
    return res
