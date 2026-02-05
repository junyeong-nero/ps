class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        res = []
        products.sort()
        l = 0
        r = len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1

            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            res.append([])
            remains = r - l + 1
            for j in range(min(3, remains)):
                res[i].append(products[l + j])

        return res


# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

#         # most 3 product names after searchword is typed.
#         m, n = len(products), len(searchWord)
#         trie = dict()

#         def add(trie, product):
#             cur = trie
#             for char in product:
#                 if char not in cur:
#                     cur[char] = dict()
#                 cur = cur[char]

#             cur["."] = product

#         def search(trie, prefix):
#             cur = trie
#             for char in prefix:
#                 if char not in cur:
#                     return []
#                 cur = cur[char]
#             return _find_all_leaves(cur)

#         def _find_all_leaves(trie):
#             res = []
#             if "." in trie:
#                 res.append(trie["."])

#             for key in trie:
#                 if key == ".":
#                     continue
#                 res += _find_all_leaves(trie[key])
#             return res


#         for product in products:
#             add(trie, product)

#         # temp = _find_all_leaves(trie)
#         # print(temp)
#         res = []

#         for i in range(1, n + 1):
#             prefix = searchWord[:i]
#             result = search(trie, prefix)
#             result = sorted(result)[:3]

#             # print(prefix, result)
#             res.append(result)

#         return res

