from typing import List


class TrieNode:
    def __init__(self):
        # child[0] = 현재 비트가 0인 쪽으로 가는 자식
        # child[1] = 현재 비트가 1인 쪽으로 가는 자식
        self.child = [None, None]

        # 이 노드를 지나가는 숫자가 현재 몇 개 들어있는지 저장
        # remove 할 때 필요하다.
        self.count = 0


class BitTrie:
    def __init__(self, max_bit: int = 17):
        # 문제에서 node index, query value 범위가 2 * 10^5 정도라
        # 17비트면 표현 가능하다. (2^18 = 262144)
        # 안전하게 17 ~ 18 정도를 많이 쓴다.
        self.root = TrieNode()
        self.max_bit = max_bit

    def insert(self, num: int) -> None:
        """
        num을 trie에 삽입한다.
        최상위 비트부터 내려가며 경로를 만든다.
        """
        node = self.root
        for b in range(self.max_bit, -1, -1):
            bit = (num >> b) & 1

            if node.child[bit] is None:
                node.child[bit] = TrieNode()

            node = node.child[bit]
            node.count += 1

    def remove(self, num: int) -> None:
        """
        num을 trie에서 제거한다.
        실제 노드를 지우지는 않고 count만 감소시킨다.
        """
        node = self.root
        for b in range(self.max_bit, -1, -1):
            bit = (num >> b) & 1
            node = node.child[bit]
            node.count -= 1

    def max_xor(self, num: int) -> int:
        """
        현재 trie에 들어있는 숫자들 중에서
        num과 XOR 했을 때 최대값을 반환한다.
        """
        node = self.root
        ans = 0

        for b in range(self.max_bit, -1, -1):
            bit = (num >> b) & 1

            # XOR를 크게 만들려면 현재 비트와 반대 비트로 가는 게 유리
            want = 1 - bit

            # 반대 비트 방향 자식이 존재하고,
            # 그 경로에 실제로 들어있는 숫자가 1개 이상 있으면 그쪽으로 간다.
            if node.child[want] is not None and node.child[want].count > 0:
                ans |= (1 << b)   # 이번 비트의 XOR 결과를 1로 만들 수 있음
                node = node.child[want]
            else:
                # 반대 비트가 없으면 같은 비트 쪽으로 갈 수밖에 없다.
                node = node.child[bit]

        return ans


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)

        # 1) 트리 구성
        children = [[] for _ in range(n)]
        root = -1

        for node, p in enumerate(parents):
            if p == -1:
                root = node
            else:
                children[p].append(node)

        # 2) 각 node에 달린 쿼리들을 모아두기
        # node_queries[u] = [(val, query_index), ...]
        node_queries = [[] for _ in range(n)]
        for i, (node, val) in enumerate(queries):
            node_queries[node].append((val, i))

        # 정답 배열
        ans = [0] * len(queries)

        # 현재 DFS 경로(root -> 현재 node)에 있는 노드 번호들을 담을 bit trie
        trie = BitTrie()

        def dfs(u: int) -> None:
            # 현재 노드를 경로에 추가
            trie.insert(u)

            # 현재 노드 u에 대한 쿼리 처리
            # trie 안에는 정확히 root ~ u 경로의 노드 번호들이 들어있다.
            for val, idx in node_queries[u]:
                ans[idx] = trie.max_xor(val)

            # 자식 탐색
            for v in children[u]:
                dfs(v)

            # DFS 복귀 시 현재 노드를 경로에서 제거
            trie.remove(u)

        dfs(root)
        return ans
