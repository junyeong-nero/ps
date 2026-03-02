def solution(a):
    MOD = 10_000_019  # 10^7 + 19

    m = len(a)
    n = len(a[0])

    # column sums
    col = [0] * n
    for i in range(m):
        row = a[i]
        for j, v in enumerate(row):
            col[j] += v

    # freq[k] = number of columns with sum k
    freq = [0] * (m + 1)
    for c in col:
        freq[c] += 1

    # factorials for C(m, r)
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact = [1] * (m + 1)
    invfact[m] = pow(fact[m], MOD - 2, MOD)
    for i in range(m, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    def comb(n_, r_):
        if r_ < 0 or r_ > n_:
            return 0
        return fact[n_] * invfact[r_] % MOD * invfact[n_ - r_] % MOD

    # inverses for 1..m+1 (for dividing by k+1 in recurrence)
    inv = [0] * (m + 2)
    for i in range(1, m + 2):
        inv[i] = pow(i, MOD - 2, MOD)

    inv_pow2m = pow(pow(2, m, MOD), MOD - 2, MOD)

    ans = 0
    for r in range(m + 1):
        mr = (m - 2 * r) % MOD  # (m - 2r)

        # build K_k(r) for k=0..m via recurrence, while accumulating product
        K_prev = 1  # K_0
        prod = pow(K_prev, freq[0], MOD)

        if m >= 1:
            K_curr = mr  # K_1
            prod = (prod * pow(K_curr, freq[1], MOD)) % MOD

            for k in range(1, m):
                # (k+1)K_{k+1} = (m-2r)K_k - (m-k+1)K_{k-1}
                K_next = (mr * K_curr - (m - k + 1) * K_prev) % MOD
                K_next = (K_next * inv[k + 1]) % MOD
                K_prev, K_curr = K_curr, K_next
                prod = (prod * pow(K_curr, freq[k + 1], MOD)) % MOD

        ans = (ans + comb(m, r) * prod) % MOD

    ans = ans * inv_pow2m % MOD
    return ans
