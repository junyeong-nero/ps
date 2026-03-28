class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        
        # 하나의 노드는 최대 2개 노드와 연결됨
        # 각 노드에 1 ~ n 까지의 값을 할당
        # score = (연결된 노드의 곱)의 합

        # cycle 이 있을 수 있다. -> edge 관점으로 접근하는게 더 나을 수 도 있음.
        # 결국 score 를 만들 때 높은 숫자 - 높은 숫자 끼리 연결하는게 최고의 상황
        # 그러면, 일단 연결된 노드 정보를 저장해서, 2개로 연결된 노드를 걸러야 함

        # 2개의 노드와 연결되어있더라도 모두 선택할 수는 없음
        # 각가의 노드가 또 걸러진 노드와 연결된 경우가 있는지 확인해야 한다.

        # 노드가 최대 2개 밖에 없다는게 큰 힌트가 될 것 같은데.
        # 결국 line or cycle 밖에 없다는 이야기 아닌가? 분기도 안되고?
        # 그러면

        m = len(edges)
        counter = Counter()

        for u, v in edges:
            counter[u] += 1
            counter[v] += 1 

        cands = set(node for node, value in counter.items() if value == 2)
        # print(cands)

        res = 0
        if n % 2 == 0:
            res += n * (n - 1)
            for i in range(n, 1, -2):
                res += i * (i - 2)
            for i in range(n - 1, 1, -2):
                res += i * (i - 2)

        else:
            res += n * (n - 1) + n * (n - 2)
            for i in range(n - 2, 1, -2):
                res += i * (i - 2)
            for i in range(n - 1, 1, -2):
                res += i * (i - 2)

        if len(cands) == m:
            res += 2

        return res

