def solution(temperature, t1, t2, a, b, onboard):
    
    # ON / OFF
    # t1 ~ t2 범위. onboard.
    # 소비전력 최소화
    
    temperature += 10
    t1 += 10
    t2 += 10
    
    n = len(onboard)
    t3 = (t1 + t2) // 2    
    delta = 1 if temperature > t3 else -1

    # 언제 킬지? 언제 끌지? 하나의 그룹으로 되어있지 않을 수 도 있는데 어떻게?
    # DP style로 풀어야지 않을까?
    # dp[i][t] : 시간(i) 온도(t) 일 때까지 소비한 최소전력
    #    onboard[i] == 1 일 때 t1 ~ t2 범위 밖에 있는 녀석들 다 날려버림
    # t : normalized ( + 10)
    
    dp = [[float("inf")] * 51 for _ in range(n + 1)]
    dp[0][temperature] = 0
    
    for i in range(1, n + 1):
    
        for t in range(51):
            if 0 <= t + delta < 51:
                dp[i][t + delta] = min(dp[i][t + delta], dp[i - 1][t])
            if 0 <= t - delta < 51:
                dp[i][t - delta] = min(dp[i][t - delta], dp[i - 1][t] + a)
            dp[i][t] = min(dp[i][t], dp[i - 1][t] + b)
                        
        if i < n and onboard[i] == 1:
            
            for t in range(0, t1):
                dp[i][t] = float("inf")
            
            for t in range(t2 + 1, 51):
                dp[i][t] = float("inf")
    
    # print(dp[-1])
    return min(dp[-1])


def solution(temperature, t1, t2, a, b, onboard):
    n = len(onboard)
    OUT = temperature + 10
    t1 += 10
    t2 += 10
    
    INF = float('inf')
    dp = [[INF] * 51 for _ in range(n + 1)]
    dp[0][OUT] = 0
    
    for i in range(1, n + 1):
        for t in range(51):
            
            if dp[i - 1][t] == INF:
                continue
            
            # 1) 에어컨 OFF: 외기온 쪽으로 1칸, 같으면 유지
            if t < OUT:
                nt = t + 1
            elif t > OUT:
                nt = t - 1
            else:
                nt = t
            dp[i][nt] = min(dp[i][nt], dp[i - 1][t])
            
            # 2) 에어컨 ON + 온도 변경
            if t > 0:
                dp[i][t - 1] = min(dp[i][t - 1], dp[i - 1][t] + a)
            if t < 50:
                dp[i][t + 1] = min(dp[i][t + 1], dp[i - 1][t] + a)
            
            # 3) 에어컨 ON + 유지
            dp[i][t] = min(dp[i][t], dp[i - 1][t] + b)
        
        # i분 시점에 사람이 타고 있으면 쾌적 범위만 허용
        if onboard[i - 1] == 1:
            for t in range(51):
                if not (t1 <= t <= t2):
                    dp[i][t] = INF
    
    return min(dp[n])


