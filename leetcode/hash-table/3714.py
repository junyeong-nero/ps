class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Result variable to store the maximum length found
        max_len = 0

        # ---------------------------------------------------------
        # Case 1: Substrings with only 1 type of character
        # (e.g., "aaa", "bb") - inherently balanced
        # ---------------------------------------------------------
        current_run = 0
        for i in range(n):
            if i > 0 and s[i] == s[i - 1]:
                current_run += 1
            else:
                current_run = 1
            max_len = max(max_len, current_run)

        # ---------------------------------------------------------
        # Case 2: Substrings with exactly 2 types of characters
        # (e.g., "aabb", "abab")
        # ---------------------------------------------------------
        def get_longest_with_two_chars(target1: str, target2: str) -> int:
            """
            Finds the longest balanced substring containing only target1 and target2.
            Any other character acts as a reset wall.
            """
            local_max = 0
            balance = 0
            # Map: balance -> first index where this balance was seen.
            # Initialize {0: -1} conceptually, but adjusted for the current segment start.
            # We use 'index - 1' logic so length = current_index - prev_index.
            seen = {0: -1} 
            
            for i, char in enumerate(s):
                if char not in (target1, target2):
                    # Reset state when a 3rd character is encountered
                    balance = 0
                    seen = {0: i}
                    continue

                # Update balance (target1 is +1, target2 is -1)
                balance += (1 if char == target1 else -1)

                if balance in seen:
                    local_max = max(local_max, i - seen[balance])
                else:
                    seen[balance] = i
            
            return local_max

        # Check all pairs: (a, b), (a, c), (b, c)
        max_len = max(max_len, get_longest_with_two_chars('a', 'b'))
        max_len = max(max_len, get_longest_with_two_chars('a', 'c'))
        max_len = max(max_len, get_longest_with_two_chars('b', 'c'))

        # ---------------------------------------------------------
        # Case 3: Substrings with all 3 types of characters
        # (e.g., "aabbcc")
        # ---------------------------------------------------------
        # We track the relative differences: (count[a]-count[b], count[a]-count[c])
        # If this tuple repeats, the substring between occurrences is balanced.
        count_a = count_b = count_c = 0
        seen_triples = {(0, 0): -1} # (diff_ab, diff_ac) -> index

        for i, char in enumerate(s):
            if char == 'a': count_a += 1
            elif char == 'b': count_b += 1
            else: count_c += 1

            key = (count_a - count_b, count_a - count_c)

            if key in seen_triples:
                max_len = max(max_len, i - seen_triples[key])
            else:
                seen_triples[key] = i

        return max_len




        # n = len(s)
        # prefix = [(0, 0, 0)] * (n + 1)
        # suffix = [(0, 0, 0)] * (n + 1)

        # cur = [0, 0, 0]
        # for i in range(n):
        #     c = s[i]
        #     cur[char2index[c]] += 1
        #     prefix[i + 1] = tuple(cur)

        # cur = [0, 0, 0]
        # for i in range(n - 1, -1, -1):
        #     c = s[i]
        #     cur[char2index[c]] += 1
        #     suffix[i] = tuple(cur)

        # # print(prefix) # counter(s[:i])
        # # print(suffix) # counter(s[i:])

        # total = [s.count("a"), s.count("b"),s.count("c")]
        # # print(total)

        # def check(i, j):
        #     temp = [(total[index] - prefix[i][index] - suffix[j][index]) for index in range(3)]
        #     temp = [elem for elem in temp if elem > 0]
        #     return len(set(temp)) == 1

        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         temp = check(i, j)
        #         if temp:
        #             # print(s[i:j], temp)
        #             res = max(res, j - i)

        # return res

        # (3, 3, 1) 을 가기 위해서 (2, 2, 0) 을 무조건 거침? -> 아님
        # 그러면 조금 문제가 있삼.

        # def find_index(j):
        #     # O(n log n)
        #     cur = prefix[j]
        #     temp = min([elem for elem in cur if elem > 0])
        #     for delta in range(temp, -1, -1):
        #         target = tuple([max(0, elem - delta) for elem in cur])
        #         i = bisect_left(prefix, target)
        #         if prefix[i] == target:
        #             return i

        #     return j

        # res = 0
        # for j in range(1, n + 1):
        #     i = find_index(j)
        #     # O(n)
        #     if i < j:
        #         print(s[i:j])
        #         print(i, j)
        #         res = max(res, j - i)

        # i = 0
        # while i < n:
        #     j = i
        #     while j + 1 < n and s[j + 1] == s[i]:
        #         j += 1

        #     res = max(res, j - i + 1)
        #     i = j + 1

        # return res

