def solution(distance, rocks, n):
    # 출발지(0)와 도착지(distance)를 포함하여 정렬
    rocks = [0] + sorted(rocks) + [distance]
    
    def check(k):
        remove_count = 0
        current_rock = 0 
        for i in range(1, len(rocks)):
            if rocks[i] - current_rock < k:
                remove_count += 1 
                if remove_count > n:
                    return False
            else:
                current_rock = rocks[i]
                
        return True 
    
    # 이분 탐색 세팅
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
            
    return right
