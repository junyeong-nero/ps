def solution(beginning, target):
    m, n = len(beginning), len(beginning[0])
    count = 0

    # row flips 결정: 첫 번째 열을 맞추는 방식
    for x in range(m):
        if beginning[x][0] != target[x][0]:
            count += 1
            for y in range(n):
                beginning[x][y] ^= 1

    # col flips 결정: 첫 번째 행을 맞추는 방식
    for y in range(n):
        if beginning[0][y] != target[0][y]:
            count += 1
            for x in range(m):
                beginning[x][y] ^= 1

    # 최종 검증 (여기서만)
    for x in range(m):
        for y in range(n):
            if beginning[x][y] != target[x][y]:
                return -1

    # (R, C)와 (complement R, complement C) 둘 다 가능하므로 최소 선택
    return min(count, m + n - count)

