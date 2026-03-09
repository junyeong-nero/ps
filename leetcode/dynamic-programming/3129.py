class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # dp0[z][o]: z개의 0, o개의 1을 사용했고 마지막이 0
        # dp1[z][o]: z개의 0, o개의 1을 사용했고 마지막이 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # base: 0만 있는 경우
        for z in range(1, min(zero, limit) + 1):
            dp0[z][0] = 1

        # base: 1만 있는 경우
        for o in range(1, min(one, limit) + 1):
            dp1[0][o] = 1

        # 점화식
        for z in range(zero + 1):
            for o in range(one + 1):
                if z == 0 and o == 0:
                    continue

                # dp0[z][o]
                if z > 0 and o > 0:
                    val = dp1[z - 1][o]
                    if z - limit - 1 >= 0:
                        val -= dp1[z - limit - 1][o]
                    dp0[z][o] = (dp0[z - 1][o] + val) % MOD

                # dp1[z][o]
                if z > 0 and o > 0:
                    val = dp0[z][o - 1]
                    if o - limit - 1 >= 0:
                        val -= dp0[z][o - limit - 1]
                    dp1[z][o] = (dp1[z][o - 1] + val) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD

# class Solution:
#     def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
#         # limits => 연속으로 limits 번 같은 숫자를 넣으면 안된다.
#         # 전체 경우의 수 (zero + one) ! / zero! one!
#         # 이중에서 limits 이상의 놈들만 거르면 되지 않을까.

#         total = factorial(zero + one) // factorial(zero) // factorial(one)
#         limit += 1

#         # 이중에서 limits 이상 연속적으로 나올 경우의 수? limits 개를 하나로 묶고
#         # 똑같이 돌려버리면 됨 limits 개의 zero 가 => 1개의 zero 로 바뀜

#         n_zero = (
#             perm(zero + one - limit + 1, 1) * factorial(zero + one - limit)
#             // factorial(zero - limit)
#             // factorial(one)
#             if zero >= limit
#             else 0
#         )

#         # (1 1 1) 0 0 0
#         #  0 0 0 
#         # ^ ^ ^ ^

#         n_one = (
#             perm(zero + one - limit + 1, 1) * factorial(zero + one - limit)
#             // factorial(zero)
#             // factorial(one - limit)
#             if one >= limit
#             else 0
#         )

#         # (1 1 1) (0 0 0)
#         #  1 0 
#         # ^ ^ ^  

#         n_intersect = (
#             perm(zero + one - limit * 2 + 2, 2) * factorial(zero + one - limit * 2)
#             // factorial(zero - limit)
#             // factorial(one - limit)
#             if one >= limit and zero >= limit
#             else 0
#         )

#         # 011
#         # 101
#         # 110

#         print(total, n_zero, n_one, n_intersect)
#         MOD = 10 ** 9 + 7
#         return (total - n_zero - n_one + n_intersect) % MOD

