class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # 결과가 매우 커질 수 있으므로 모듈러 연산 사용
        MOD = 10**9 + 7

        # dp0[z][o]:
        # 0을 z개, 1을 o개 사용해서 만든 안정적인 배열의 개수 중
        # 마지막 원소가 0인 경우의 수
        #
        # dp1[z][o]:
        # 0을 z개, 1을 o개 사용해서 만든 안정적인 배열의 개수 중
        # 마지막 원소가 1인 경우의 수
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # base case 1: 0만 사용하는 경우
        # 연속된 같은 숫자의 개수가 limit 이하일 때만 가능하므로
        # 길이가 1 ~ min(zero, limit)인 경우만 1개씩 존재
        for z in range(1, min(zero, limit) + 1):
            dp0[z][0] = 1

        # base case 2: 1만 사용하는 경우
        # 마찬가지로 길이가 limit 이하일 때만 가능
        for o in range(1, min(one, limit) + 1):
            dp1[0][o] = 1

        # 모든 (z, o) 상태를 순회하면서 점화식으로 채움
        for z in range(zero + 1):
            for o in range(one + 1):
                # 아무 숫자도 사용하지 않은 빈 배열은 제외
                if z == 0 and o == 0:
                    continue

                # dp0[z][o] 계산:
                # 마지막이 0인 배열의 개수
                if z > 0 and o > 0:
                    # 마지막에 0을 붙이는 경우를 생각한다.
                    #
                    # 기본적으로 dp1[z - 1][o]에서 시작:
                    # 0을 하나 추가하기 전 상태는 반드시 마지막이 1이어야
                    # 연속 구간이 새로 시작된다고 볼 수 있다.
                    val = dp1[z - 1][o]

                    # 그런데 0이 limit개를 초과해서 연속되는 경우는 빼줘야 한다.
                    # 즉, 끝에 0이 (limit + 1)개 이상 붙는 경우 제거
                    #
                    # 누적 방식으로 dp0[z - 1][o] + val 을 쓰고 있으므로
                    # 범위를 벗어나는 오래된 값(dp1[z - limit - 1][o])을 빼준다.
                    if z - limit - 1 >= 0:
                        val -= dp1[z - limit - 1][o]

                    # dp0[z - 1][o]는 이전까지의 누적값 역할
                    # val은 이번 z에서 새롭게 추가되는 유효한 경우의 수
                    dp0[z][o] = (dp0[z - 1][o] + val) % MOD

                # dp1[z][o] 계산:
                # 마지막이 1인 배열의 개수
                if z > 0 and o > 0:
                    # 마지막에 1을 붙이는 경우를 생각한다.
                    # 이전 상태는 마지막이 0이어야 한다.
                    val = dp0[z][o - 1]

                    # 1이 limit개를 초과해서 연속되는 경우 제거
                    if o - limit - 1 >= 0:
                        val -= dp0[z][o - limit - 1]

                    # 마찬가지로 누적합 방식으로 계산
                    dp1[z][o] = (dp1[z][o - 1] + val) % MOD

        # 마지막이 0인 경우 + 마지막이 1인 경우를 합쳐 전체 정답 반환
        return (dp0[zero][one] + dp1[zero][one]) % MOD
