class Solution:
    def minJumps(self, nums: List[int]) -> int:
        
        n = len(nums)

        # operations:
        # 1. jump to adj (+1, -1)
        # 2. teleport if nums[i] == p is prime, move to j s.t. nums[j] % p == 0

        # design
        # - prime factorizatoin all nums
        # - BFS approach for shortest path to n - 1 index
        #   - queue[(start, dist)] -> start + 1, dist + 1

        # constraints
        # - n = 10^5
        # - solve in O(n log n)

        # time complexity
        # prime factorizatoin all nums - O(n log n)
        # BFS - O(n)

        @cache
        def prime_facto(n):
            factors = Counter()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors[d] += 1
                    n //= d
                d += 1
            if n > 1:
                factors[n] += 1
            return factors

        d = defaultdict(list)
        is_prime = [False] * n
        # d[prime] : a list of index s.t. num[index] % p == 0

        for i, num in enumerate(nums):
            temp = prime_facto(num)
            if sum(temp.values()) == 1:
                is_prime[i] = True

            for prime in temp:
                d[prime].append(i)


        visited = [float("inf")] * n
        visited[0] = 0

        q = deque([(0, 0)])

        while q: 
            # print(q)

            cur, dist = q.popleft()
            if cur == n - 1:
                return dist

            new_dist = dist + 1

            # op1: adj
            if cur + 1 < n and new_dist < visited[cur + 1]:
                visited[cur + 1] = new_dist
                q.append((cur + 1, new_dist))

            if cur - 1 >= 0 and new_dist < visited[cur - 1]:
                visited[cur - 1] = new_dist
                q.append((cur - 1, new_dist))

            # op2: teleportation
            if is_prime[cur]:
                for j in d[nums[cur]]:
                    if cur == j: continue
                    if new_dist < visited[j]:
                        visited[j] = new_dist
                        q.append((j, new_dist))
                
                # pruning : only one teleporation.
                d[nums[cur]].clear()
            
        return -1


    # TC
    # [1, 1, 1, 1, 1, ..., 1, 1]

