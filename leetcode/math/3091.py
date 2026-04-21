class Solution:
    def minOperations(self, k: int) -> int:

        # operations
        # - choose any element and increase 1
        # - duplicate and append at the end
        # minimum steps for sum(nums) >= k

        # 그러면 어짜피 가장 최단 시간으로 올려야 할거라면,
        # 최대값에만 집중하면 될 것 같은데. 굳이 작은걸 복사할 필요없으니까?

        # 더 생각을 해보면.. 하나에만 + 1 을 반복한 다음 k 번 복제하면 끝?
        # (1 + a) * b >= k
        # b >= k / (1 + a)
        # minimize (a + b)

        res = k - 1

        for a in range(k):
            b = int(math.ceil(k / (1 + a)))
            res = min(res, a + b - 1)

        return res


        # sum, max_value
        q = deque([(1, 1)])
        step = 0
        complete = False

        while not complete:

            # print(q)

            for _ in range(len(q)):

                total, value = q.popleft()
                if total >= k:
                    complete = True
                    break
                    
                q.append((total + 1, value + 1))
                q.append((total + value, value))

            if complete:
                break
            step += 1

        return step

