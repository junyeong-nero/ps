class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:

        n = len(edges) + 1
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        guess_set = set((u, v) for u, v in guesses)

        # 1) root = 0 일 때 맞는 guess 수 계산
        def dfs_count(u: int, parent: int) -> int:
            count = 0
            for v in graph[u]:
                if v == parent:
                    continue
                if (u, v) in guess_set:
                    count += 1
                count += dfs_count(v, u)
            return count

        initial = dfs_count(0, -1)

        # 2) reroot 하면서 각 노드가 루트일 때 맞는 guess 수 계산
        ans = 0

        def dfs_reroot(u: int, parent: int, cur: int) -> None:
            nonlocal ans

            if cur >= k:
                ans += 1

            for v in graph[u]:
                if v == parent:
                    continue

                nxt = cur

                # u -> v 가 뒤집히므로 영향 반영
                if (u, v) in guess_set:
                    nxt -= 1
                if (v, u) in guess_set:
                    nxt += 1

                dfs_reroot(v, u, nxt)

        dfs_reroot(0, -1, initial)
        return ans


        ### BFS + Pruned Version

        n = len(edges) + 1
        d = [0] * n

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)



        def get_parents(guess_idx):
            parent, child = guesses[guess_idx]

            q = deque([parent])
            visited = set()
            visited.add(child)

            while q:
                cur = q.popleft()
                d[cur] += 1
                visited.add(cur)

                for node in graph[cur]:
                    if node in visited: continue
                    
                    # 여기도 개선할 수 있을 것 같음.
                    # 지금 child - parent 이용해서 자꾸 parents 를 찾도록 하는데
                    # traverse 과정에서 guesses 에 포함된 다른 (child, parent) 를 만나면
                    # 이걸 어떻게 최적화할 수 있지 않을까?

                    q.append(node)
            
            return visited

        for i in range(len(guesses)):
            get_parents(i)

        return sum([1 for num in d if num >= k])


        ### BFS Approach (naive)

        d = defaultdict(set)
        for parent, child in guesses:
            d[parent].add(child)

        # O(n log n)
        # graph traverse => O(n)
        # check in O(log n)
        # - requires pruning! 

        # at least k

        def check(node):
            q = deque([node])
            visited = [False] * n
            count = 0
            
            while q:

                cur = q.popleft()
                visited[cur] = True

                for node in graph[cur]:
                    if visited[node]: continue
                    if node in d[cur]:
                        count +=  1
                    q.append(node)

            return count >= k

        res = 0
        for node in graph:
            temp = check(node)
            if temp:
                res += 1

        return res
                    


