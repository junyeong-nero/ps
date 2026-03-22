def solution(commands):
    SIZE = 50
    N = SIZE * SIZE + 1  # 1-based index

    parent = [i for i in range(N)]
    value = [""] * N  # 값은 root에만 저장

    def idx(r, c):
        return (r - 1) * SIZE + c

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return

        # 병합 후 어떤 값을 유지할지 결정
        # 문제 조건:
        # - 두 셀 모두 값이 있으면 (r1, c1)의 값 유지
        # - 한쪽만 값 있으면 그 값 유지
        # - 둘 다 없으면 빈 값
        if value[ra]:
            keep = value[ra]
        else:
            keep = value[rb]

        parent[rb] = ra
        value[ra] = keep
        value[rb] = ""

    answer = []

    for command in commands:
        args = command.split()

        if args[0] == "UPDATE":
            if len(args) == 4:
                # UPDATE r c value
                r, c, v = int(args[1]), int(args[2]), args[3]
                root = find(idx(r, c))
                value[root] = v
            else:
                # UPDATE value1 value2
                v1, v2 = args[1], args[2]
                for i in range(1, N):
                    if parent[i] == i and value[i] == v1:
                        value[i] = v2

        elif args[0] == "MERGE":
            r1, c1, r2, c2 = map(int, args[1:])
            a = idx(r1, c1)
            b = idx(r2, c2)
            union(a, b)

        elif args[0] == "UNMERGE":
            r, c = int(args[1]), int(args[2])
            x = idx(r, c)
            root = find(x)
            saved = value[root]

            # 같은 그룹에 속한 모든 셀 찾기
            members = []
            for i in range(1, N):
                if find(i) == root:
                    members.append(i)

            # 전부 분리
            for m in members:
                parent[m] = m
                value[m] = ""

            # 지정 셀만 기존 값 유지
            value[x] = saved

        elif args[0] == "PRINT":
            r, c = int(args[1]), int(args[2])
            root = find(idx(r, c))
            answer.append(value[root] if value[root] else "EMPTY")

    return answer
