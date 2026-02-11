def solution(gems):
    n = len(set(gems))
    answer = [1, len(gems)]
    
    hist = {}
    i = 0  # 왼쪽 포인터
    
    for j, gem in enumerate(gems): # j는 오른쪽 포인터
        # 1. 오른쪽 포인터 이동하며 보석 추가
        hist[gem] = hist.get(gem, 0) + 1
        
        # 2. 모든 종류의 보석이 다 모였을 때
        while len(hist) == n:
            # 3. 현재 구간이 기존 정답보다 짧으면 갱신
            if j - i < answer[1] - answer[0]:
                answer = [i + 1, j + 1]
            
            # 4. 왼쪽 포인터를 당기며 구간 축소
            left_gem = gems[i]
            hist[left_gem] -= 1
            if hist[left_gem] == 0:
                del hist[left_gem]
            i += 1
            
    return answer

# def solution(gems):
    
#     n = len(set(gems))
#     res = [1, len(gems)]
#     hist = {}
    
#     for j, gem in enumerate(gems):
#         hist[gem] = j
#         if len(hist) != n:
#             continue
#         i = min(hist.values()) 
#         if j - i < res[1] - res[0]:
#             res = [i + 1, j + 1]
    
#     return res
