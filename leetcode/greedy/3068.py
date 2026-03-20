class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        n = len(nums)

        # 결국 노드에 XOR 을 할지 말지 결정하는 문제
        # 연결된 노드를 한 번에 뒤집어야 하고, 최대 횟수 제한이 없으니 사실 어떤 노드를 뒤집을지 선택하면 된다.
        # 그리고 한 번 뒤집을 때 연결된 노드가 함께 뒤집히니 뒤집는 노드의 개수는 무조건 짝수여야 한다.
        # 뒤집었을 때 커지는 node 의 개수를 파악하고 이게 짝수라면 그대로 고.
        # 만약 홀수라면 그래도 가장 작은 수를 빼고 다 뒤집으면 된다.

        base = sum(nums)
        gains = [(x ^ k) - x for x in nums]

        pos_sum = 0
        pos_cnt = 0
        min_pos = float('inf')
        max_nonpos = -float('inf')

        for g in gains:
            if g > 0:
                pos_sum += g
                pos_cnt += 1
                min_pos = min(min_pos, g)
            else:
                max_nonpos = max(max_nonpos, g)

        if pos_cnt % 2 == 0:
            return base + pos_sum

        return base + max(pos_sum - min_pos, pos_sum + max_nonpos)

        # 이어진 두 개의 노드를 골라서 XOR을 수행
        # n = 2 * 10^4

        # tree 의 형태를 띄고 있다.
        # leaf node 를 업데이트 하면 parents 로 전파되는 형식
        # xor 을 두 번 하면 자기자신으로 돌아옴.
        # levels 로 나누면 좋을 것 같은데
        # 결국 leaf node의 경우에 xor 을 해서 커진다면 무조건 하는게 좋음
        # 그리고 이게 parents level 로 올라가고 이건 이제 자연스럽게 parents 로 전파됨.

        res = sum(nums)

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = [(node, 0) for node in graph if len(graph[node]) == 1]

        q = deque(leaves)
        visited = set()

        while q:

            print(q)
            parents = Counter()

            for _ in range(len(q)):

                cur, update = q.popleft()
                visited.add(cur)

                check = 1 if nums[cur] ^ k > nums[cur] else 0
                if check:
                    nums[cur] ^= k
                if check & 1 != update & 1:
                    update += 1

                for node in graph[cur]:
                    if node in visited:
                        continue
                    parents[node] += update 
            
            for parent, update in parents.items():
                if parent in visited:
                    continue
                q.append((parent, update))

        print(nums)
        res = max(res, sum(nums))
        return res


