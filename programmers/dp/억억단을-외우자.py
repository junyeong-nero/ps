def solution(e, starts):
    # 1. 약수 개수 배열 (가장 빠른 O(sqrt(E) * log E) 방식)
    div_count = [0] * (e + 1)
    
    # i는 1부터 sqrt(e)까지만 순회
    for i in range(1, int(e**0.5) + 1):
        # i * i는 제곱수이므로 약수가 1개(자기 자신) 추가됨
        div_count[i * i] += 1
        
        # i * i 보다 큰 i의 배수들은 약수 쌍(i, j//i)이 2개씩 존재함
        # 예) i=2일 때 2*3=6 -> 약수 2와 3이 동시에 발견된 것으로 치고 +2를 해줌
        for j in range(i * i + i, e + 1, i):
            div_count[j] += 2

    # 2. DP 배열 구성 (튜플 대신 1차원 리스트 2개를 써서 속도/메모리 최적화)
    max_count = [0] * (e + 1)  # 해당 구간의 최대 약수 개수
    max_idx = [0] * (e + 1)    # 해당 구간의 최대 약수를 가진 숫자
    
    max_count[e] = div_count[e]
    max_idx[e] = e
    
    # 3. 뒤에서부터 앞으로 오면서 DP 테이블 채우기
    # starts 최솟값까지만 구하면 되지만, 편의상 1까지 전부 구함
    for i in range(e - 1, 0, -1):
        if div_count[i] >= max_count[i + 1]:
            max_count[i] = div_count[i]
            max_idx[i] = i
        else:
            max_count[i] = max_count[i + 1]
            max_idx[i] = max_idx[i + 1]
            
    # 4. 정답 쿼리 처리
    res = []
    for s in starts:
        res.append(max_idx[s])
        
    return res

# def func(k):
#     res = 1
#     for i in range(2, int(k ** 0.5) + 1):
#         count = 0
#         while k % i == 0:
#             k //= i
#             count += 1
#         res *= (count + 1)
#     if k > 1:
#         res *= 2 
#     return res
    
    
# def solution(e, starts):
#     answer = []
    
#     # s <= x <= e
#     # 가장 많이 등장 -> 두 개의 수로 인수분해되었을 때 경우의 수가 가장 많음
#     # x = a^x * b^y * c^z ... 일 때
#     # 1 * (a^x * b^y * c^z) / a (a^(x - 1) * b^y * c^z) ... / 이런식으로
#     # x, y, z 중에서 x, y, z는... 같은 아이템으로 취급됨.
#     # (x + 1) * (y + 1) * (z + 1) 이런식으로? 
#     s = min(starts)

#     dp = {e:(func(e), e)}
#     # dp[i] : [i, e] 사이에서 most freq
#     for i in range(e, s, -1):
#         temp = func(i - 1)
#         if temp >= dp[i][0]:
#             dp[i - 1] = (temp, i - 1)
#         else:
#             dp[i - 1] = dp[i]
        
#     res = []
#     for s in starts:
#         res.append(dp[s][1])
        
#     return res 
