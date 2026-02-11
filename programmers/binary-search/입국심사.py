def solution(n, times):
    # 최선의 경우: 1분
    # 최악의 경우: 가장 느린 심사관이 모든 사람을 다 처리할 때
    left = 1
    right = max(times) * n 
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간 동안 심사할 수 있는 총 인원 수 계산
        people = sum(mid // time for time in times)
        
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer
