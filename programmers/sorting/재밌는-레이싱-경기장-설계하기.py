def solution(heights):
    h = sorted(heights)
    n = len(h)
    if n <= 1:
        return 0

    m = n // 2

    # d_i = h[i+m] - h[i]
    diffs = [h[i + m] - h[i] for i in range(m)]

    if n % 2 == 0:
        # 짝수: 최소값이 답
        return min(diffs)

    # 홀수: J = h[-1], b1 = h[m]
    diffs.append(h[-1] - h[m])

    diffs.sort()
    return diffs[1]  # 두 번째로 작은 값
