def solution(n, k, cmd):
    # prev[i], next[i]는 i행의 이전/다음 "살아있는" 행을 가리킴
    prev = [i - 1 for i in range(n)]
    nxt = [i + 1 for i in range(n)]
    nxt[n - 1] = -1

    alive = ["O"] * n
    stack = []
    cur = k

    for q in cmd:
        op = q[0]

        if op == "U":
            x = int(q[2:])
            for _ in range(x):
                cur = prev[cur]

        elif op == "D":
            x = int(q[2:])
            for _ in range(x):
                cur = nxt[cur]

        elif op == "C":
            # 현재 행 삭제
            stack.append((cur, prev[cur], nxt[cur]))
            alive[cur] = "X"

            p, n_ = prev[cur], nxt[cur]

            # 연결 끊기
            if p != -1:
                nxt[p] = n_
            if n_ != -1:
                prev[n_] = p

            # 커서 이동: 아래가 있으면 아래, 없으면 위
            cur = n_ if n_ != -1 else p

        else:  # "Z"
            i, p, n_ = stack.pop()
            alive[i] = "O"

            # 연결 복구
            if p != -1:
                nxt[p] = i
            if n_ != -1:
                prev[n_] = i
            prev[i] = p
            nxt[i] = n_

    return "".join(alive)
