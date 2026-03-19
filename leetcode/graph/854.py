class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:

        ### BFS + Pruning
        
        if s1 == s2:
            return 0

        q = deque([(s1, 0)])
        visited = {s1}

        while q:
            cur, dist = q.popleft()

            if cur == s2:
                return dist

            # 첫 mismatch 찾기
            i = 0
            while cur[i] == s2[i]:
                i += 1

            cur_list = list(cur)

            # cur[i]를 바로 고칠 수 있는 swap만 시도
            for j in range(i + 1, len(cur)):
                if cur[j] == s2[i] and cur[j] != s2[j]:
                    nxt = cur_list[:]
                    nxt[i], nxt[j] = nxt[j], nxt[i]
                    nxt_str = "".join(nxt)

                    if nxt_str not in visited:
                        visited.add(nxt_str)
                        q.append((nxt_str, dist + 1))
        
        ### Graph + BFS + Cycle Detection

        # 조금더 수학적으로 생각해보자. 어떻게 하면 smallest k 를 찾을 수 있을까?
        # 일단 s1[i] == s2[i] 인 경우에는 안바꿔도 된다. 
        # s1[i] != s2[i] 인 경우가 문제인데, 가장 optimal 한 경우는
        # s1[i] == s2[j], s1[j] == s2[i] 인 index i, j 를 찾는 것.
        # 가장 효율 좋게 바꿀 수 있다.

        # abcde
        # edcba
        # answer = 2

        # abcdef
        # fedcba
        # answer = 3

        # abc
        # bca
        # answer = 2

        n = len(s1)
        res = 0
        d = defaultdict(list)
        solved = [True] * n

        for i in range(n):
            if s1[i] != s2[i]:
                res += 1
                solved[i] = False
                d[s1[i]].append(i)

        print(d)
        # s[i] => d[s[i]] 중 하나 와 swap 을 해야 됨
        # 어떻게 보면 cycle detection 인 것 같은데?
        # 자기자신으로 돌아오는 최단 경로 찾기.

        def find_cycle(index):
            
            q = deque([(0, index)])
            visited = dict()
            visited[index] = -1
            parent = [-1] * n

            while q:
                
                cur_dist, cur = q.popleft()

                for j in d[s2[cur]]:
                    if j == index:
                        # print(visited)
                        return cur, visited
                    if j in visited or solved[j]:
                        continue
                    
                    visited[j] = cur
                    q.append((cur_dist + 1, j))

            return -1


        def merge(index):
            end, maps = find_cycle(index)
            history = [end]
            while maps[history[-1]] != -1:
                history.append(maps[history[-1]])

            # print(index, history)
            for node in history:
                solved[node] = True

            return len(history) - 1

        res = 0

        for i in range(n):
            if solved[i]:
                continue

            temp = merge(i)
            # print(i, temp)
            res += temp

        return res

        ### Naive BFS

        # 일단 모든 경우의 수를 해보기에는 무리가 있다.
        # 문자열의 길이가 20 미만이긴 하지만, 어떤 index i, j 를 고를 때는 20^2 이고
        # 이것들을 최대 k번 반복해야 됨. -> 가능할지도 ?
        # 문자열들도 abcdef 밖에 없다. 
        # 그러면 일단 dijkstra 로 시도해보자.

        # str 그대로 사용하는건 좀 별로인듯 한데 다른 데이터구조로 저장을 해야 swap 도 편하게 할 것 같다.
        # 이 방식은 MLE 발생함. 하긴 당연하지.

        def convert(s):
            return [ord(c) - ord("a") for c in s]

        s1, s2 = convert(s1), convert(s2)

        n = len(s1)
        
        q = [(0, s1)]
        visited = set()
        visited.add(tuple(s1))

        while q:
            
            cur_dist, cur = heappop(q)
            visited.add(tuple(cur))
            if cur == s2:
                return cur_dist

            for i in range(n):
                for j in range(i):

                    new_str = cur[:]
                    new_str[i], new_str[j] = new_str[j], new_str[i]
                    if tuple(new_str) in visited:
                        continue

                    heappush(q, (cur_dist + 1, new_str))

        return -1


