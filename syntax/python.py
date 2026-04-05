import random
import math
import heapq

from collections import deque, Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, accumulate, product
from functools import lru_cache


def main():
    pass


def defaultdict_example():
    graph = defaultdict(list)
    edges = [(1, 2), (2, 3), (1, 3)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print(dict(graph))


def counter_example():
    arr1 = []
    arr2 = []
    for i in range(1, 10):
        arr1 += [i] * random.randint(1, 10)
        arr2 += [i] * random.randint(1, 10)

    counter1 = Counter(arr1)
    print(counter1)
    counter2 = Counter(arr2)
    print(counter2)

    print(counter1 + counter2)
    print(counter1 - counter2)


def deque_example():
    q = deque([(1, 2)])

    q.appendleft((3, 4))
    q.append((5, 6))
    q.popleft()
    q.pop()

    q.clear()


def heapq_example():
    pq = []
    heapq.heappush(pq, (2, "b"))
    heapq.heappush(pq, (1, "a"))
    heapq.heappush(pq, (3, "c"))

    while pq:
        print(heapq.heappop(pq))


def itertools_example():
    arr = [1, 2, 3]

    print(list(permutations(arr, 2)))
    print(list(combinations(arr, 2)))
    print(list(accumulate(arr)))
    print(list(product([1, 2], repeat=2)))


def functools_example():
    @lru_cache(None)
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    print(fib(10))


def math_example():
    print(math.gcd(12, 18))
    print(math.comb(5, 2))
    print(math.sqrt(81))
    print(math.ceil(3.14))
    print(math.floor(3.14))


def set_example():
    s = set()

    s.add(1)
    s.add(2)
    s.add(2)
    print(s)  # {1, 2}

    a = {1, 2, 3}
    b = {3, 4, 5}

    print(a | b)  # 합집합
    print(a & b)  # 교집합
    print(a - b)  # 차집합
    print(2 in a)  # 포함 여부


def list_example():
    arr = [3, 1, 4, 1, 5]

    arr.append(9)
    arr.extend([2, 6])
    arr.sort()
    print(arr)

    print(arr[0])  # 첫 원소
    print(arr[-1])  # 마지막 원소
    print(arr[:3])  # 슬라이싱

    arr.reverse()
    print(arr)

    print(arr.count(1))
    print(arr.index(5))


if __name__ == "__main__":
    main()
