from itertools import permutations

def solution(n, submit):
    # 1. 1~9 중 '서로 다른 4개의 숫자'로 이루어진 모든 경우의 수 (총 3024개)
    # 0이 포함되거나 중복된 숫자가 있는 경우는 완전히 제외됩니다.
    cands =["".join(p) for p in permutations("123456789", 4)]

    # 2. 제출 결과(예: "1S 2B")와 완벽히 똑같은 포맷의 문자열을 반환하는 함수
    def get_score(secret, guess):
        # 스트라이크: 위치와 숫자가 모두 일치하는 개수
        strike = sum(s == g for s, g in zip(secret, guess))
        
        # 서로 다른 숫자들로만 구성되어 있으므로, set의 교집합 길이 = 전체 일치하는 숫자의 개수
        total_match = len(set(secret) & set(guess))
        ball = total_match - strike
        
        return f"{strike}S {ball}B"

    for _ in range(n):
        # 3. 후보가 1개만 남았다면 굳이 submit 횟수를 소모하지 않고 즉시 반환
        if len(cands) == 1:
            return int(cands[0])
            
        guess = cands[0]
        
        # 4. 정수로 submit 하고 문자열 결과를 받음
        res = submit(int(guess))

        # 4 스트라이크면 무조건 정답
        if res == "4S 0B":
            return int(guess)

        # 5. 방금 제출한 결과와 동일한 결과를 낼 수 있는 진짜 후보들만 남기고 쳐냄
        cands =[cand for cand in cands if get_score(cand, guess) == res]

    # 반복문이 종료될 때까지 못 찾았다면 최후에 남은 하나를 정답으로 반환
    return int(cands[0]) if cands else -1
