from functools import lru_cache
import sys

# 재귀 깊이 제한 해제 (n=40인 경우 필요)
sys.setrecursionlimit(2000)


def solution(s1, s2):
    n = len(s1)

    @lru_cache(None)
    def dp(idx, bal1, bal2, min_bal2):
        # 모든 인덱스를 다 확인했을 때
        if idx == n:
            # 1. s1의 전체 balance는 bal1입니다.
            # 2. s2 과정 중 가장 낮았던 지점은 bal1 + min_bal2 입니다.
            # 3. 최종 합(bal1 + bal2)은 0이어야 합니다.
            if bal1 + min_bal2 >= 0 and bal1 + bal2 == 0:
                return 1
            return 0

        # 결과값 저장 (현재 인덱스를 무시하는 경우)
        res = dp(idx + 1, bal1, bal2, min_bal2)

        # 현재 인덱스를 선택하는 경우
        # s1의 prefix balance 체크
        char1 = s1[idx]
        delta1 = 1 if char1 == "(" else -1
        new_bal1 = bal1 + delta1

        if new_bal1 >= 0:  # s1 부분은 중간에 0 미만으로 떨어지면 안 됨
            char2 = s2[idx]
            delta2 = 1 if char2 == "(" else -1
            new_bal2 = bal2 + delta2
            # s2의 상대적 최솟값 갱신
            new_min_bal2 = min(min_bal2, new_bal2)
            res += dp(idx + 1, new_bal1, new_bal2, new_min_bal2)

        return res

    return dp(0, 0, 0, 0)


if __name__ == "__main__":
    # n=20 예시
    print(solution("((((((((((((((((((((", "))))))))))))))))))))"))
