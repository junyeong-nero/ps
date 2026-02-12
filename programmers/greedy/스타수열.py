from collections import Counter

def solution(a):
    answer = 0
    # 1. 각 숫자의 빈도수를 구합니다.
    counts = Counter(a)
    
    # 2. 각 숫자(k)를 교집합 원소라고 가정하고 탐색
    for k in counts.keys():
        # [가지치기]
        # 해당 숫자의 등장 횟수(counts[k])가 현재 찾은 정답의 절반 이하라면
        # 이 숫자로 아무리 잘 만들어도 현재 정답을 넘을 수 없으므로 스킵 (이게 없으면 시간초과 가능성 높음)
        if counts[k] * 2 <= answer:
            continue
        
        length = 0
        idx = 0
        
        # 3. 배열 전체를 훑으며 그리디하게 짝을 짓습니다.
        while idx < len(a) - 1:
            # 짝이 되기 위한 조건
            # (1) a[idx]와 a[idx+1] 둘 중 하나는 k여야 함 (교집합 원소 포함)
            # (2) a[idx]와 a[idx+1]은 서로 달라야 함 (문제 조건)
            if (a[idx] == k or a[idx+1] == k) and (a[idx] != a[idx+1]):
                length += 2
                idx += 2 # 짝을 만들었으므로 두 칸 이동
            else:
                idx += 1 # 짝을 못 만들었으므로 한 칸 이동해서 다시 시도
        
        answer = max(answer, length)
        
    return answer
