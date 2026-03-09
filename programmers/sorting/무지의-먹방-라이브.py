from collections import Counter

def solution(food_times, k):
    # 1. k가 전체 음식을 먹는 시간보다 크거나 같으면 더 이상 먹을 음식이 없음
    if sum(food_times) <= k:
        return -1
    
    n = len(food_times)
    
    # 2. 중복을 제거한 오름차순 배열 (높이 차이만 계산하기 위함)
    arr = sorted(list(set(food_times)))
    counter = Counter(food_times)
    
    index = 0
    size = n # 현재 남아있는 음식의 개수
    prev_height = 0 # 이전에 깎아낸 높이
    
    while True:
        # 이번에 깎아낼 높이 = 현재 높이 - 이전 높이
        height_diff = arr[index] - prev_height
        temp = size * height_diff
        
        # 남은 시간(k)이 이번 사이클을 다 돌기엔 부족하다면 탈출
        if k < temp:
            break
            
        k -= temp
        size -= counter[arr[index]] # 이번 높이에서 다 먹고 사라지는 음식 개수 빼기
        prev_height = arr[index]    # 이전 높이 갱신
        index += 1
    
    # 3. k가 남은 음식 개수보다 클 수 있으므로 나머지 연산 필수!
    k %= size
    
    # 4. 남은 음식들 중에서 k번째 음식 찾기
    for i, time in enumerate(food_times):
        # 현재 기준 높이(arr[index])보다 큰 음식만 아직 남아있는 음식임
        if time >= arr[index]:
            if k == 0:
                return i + 1 # 1-based index이므로 +1
            k -= 1
            
    return -1
