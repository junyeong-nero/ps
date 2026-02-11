def solution(A, B):
    
    # A[i] -> B[i] > A[i] 중 가장 최소의 수.
    # dp[i] = maximum score with A[:i] and B[:i]
    # dp[0] = 0
    # dp[i] = dp[i - 1] + (1 if A[i - 1] < B[i - 1] else 0)
    # 아닌 경우에 문제가 된다.
    # A 에서 못 이겨먹은 숫자를 바탕으로 업데이트를 해줘야 함.
    #  -> DP 로 푸는 건 힘들어보임
    # A : [5, 1, 3] + [7] => [5, 1, 3 ,7]
    # B : [6, 2, 2] + [5] => [6, 2, 5, 2]
    
    # sorted ?
    
    # padding = 0
    # A: 1, 3, 5, 7 
    # B: 2, 2, 6, 8
    # score: 3
    
    # indexing 을 바꾸면 될듯?
    
    # padding = 1
    # A:    1, 3, 5, 7 
    # B: 2, 2, 6, 8
    # score : 3
    
    # padding = 2
    # A:       1, 3, 5, 7 
    # B: 2, 2, 6, 8
    # score : 2 
    # break.
    
    n = len(B)
    A = sorted(A)
    B = sorted(B)
    
    def get_score(index=0):
        score = 0
        for i in range(n):
            a = A[i - index] if i - index >= 0 else float("inf")
            b = B[i]
            if b > a:
                score += 1
        return score
    
    start, end = 0, n - 1
    while start < end:
        mid = (start + end) // 2
        if get_score(mid) < get_score(mid + 1):
            start = mid + 1
        else:
            end = mid
            
    # print(start, end)
    answer = get_score(start)
    return answer
