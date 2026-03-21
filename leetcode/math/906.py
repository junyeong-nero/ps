class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:

        L = int(left)
        R = int(right)

        def is_palindrome(x: int) -> bool:
            s = str(x)
            return s == s[::-1]

        def make_odd_palindrome(seed: int) -> int:
            s = str(seed)
            return int(s + s[-2::-1])   # 마지막 자리 제외하고 뒤집기

        def make_even_palindrome(seed: int) -> int:
            s = str(seed)
            return int(s + s[::-1])

        ans = 0
        limit = int(R ** 0.5)

        # seed upper bound:
        # palindrome root <= 1e9 정도라서 seed는 대략 10^5 정도면 충분
        # (홀수/짝수 팰린드롬 생성 기준)
        for seed in range(1, 100000):
            # 홀수 길이 팰린드롬 root
            p = make_odd_palindrome(seed)
            if p > limit:
                break
            sq = p * p
            if sq >= L and is_palindrome(sq):
                ans += 1

        for seed in range(1, 100000):
            # 짝수 길이 팰린드롬 root
            p = make_even_palindrome(seed)
            if p > limit:
                break
            sq = p * p
            if sq >= L and is_palindrome(sq):
                ans += 1

        return ans

        ### String-based Approach

        cur = list(left)

        @cache
        def func(digit):
            if digit == 0:
                return [""]
            if digit == 1:
                return list("0123456789")

            res = []
            origin = func(digit - 2)
            for i in range(10):
                for num in origin:
                    res.append(str(i) + num + str(i))

            return res

        for digit in range(len(left), len(right) + 1):
            temp = func(digit)
            temp = [
                int(num)
                for num in temp
                if num[0] != "0" and sqrt(int(num)) - int(sqrt(int(num))) <= 10e-7
            ]
            print(temp)

        return 0

        ### BFS Aproach, generate candidates

        # palindrome check
        # filtering squares

        n_left, n_right = int(left), int(right)
        palindromes = []

        q = deque([""])
        while q:
            cur = q.popleft()

            temp = [int(cur + cur[::-1])] if cur != "" else []
            temp += [int(cur + str(i) + cur[::-1]) for i in range(10)]

            temp = [
                elem
                for elem in temp
                if n_left <= elem <= n_right and sqrt(elem) - int(sqrt(elem)) <= 10e-7
            ]
            palindromes += temp

            start = 1 if cur == "" or int(cur) == 0 else 0
            for i in range(start, 10):
                if len(cur) + 1 > len(right) // 2:
                    continue
                q.append(cur + str(i))

        # print(palindromes)

        super_palindromes = []
        for num in palindromes:
            temp = str(int(sqrt(num)))
            if temp == temp[::-1]:
                super_palindromes.append(num)

        # print(super_palindromes)
        return len(super_palindromes)

