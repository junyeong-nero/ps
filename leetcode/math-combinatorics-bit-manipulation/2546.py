class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target:
            return True
        return ('1' in s) and ('1' in target)


# class Solution:
#     def makeStringsEqual(self, s: str, target: str) -> bool:
#         # with i, j
#         # s[i] = s[i] | s[j]
#         # s[j] = s[i] ^ s[j]

#         # is it convert from s to target?

#         # s[i] = 0 / s[j] = 0 => s[i] = 0 / s[j] = 0
#         # s[i] = 0 / s[j] = 1 => s[i] = 1 / s[j] = 1
#         # s[i] = 1 / s[j] = 0 => s[i] = 1 / s[j] = 1
#         # s[i] = 1 / s[j] = 1 => s[i] = 1 / s[j] = 0

#         # s[i] = 1 으로 변하면 절대로 다시 s[i] = 0 이 될 수 없음.
#         # 0 -> 1 로 바꾸기 위해서는 s[j] == 1 이 있어야 함.
#         # 1 -> 0 로 바꾸기 위해서는 s[i] == 1 이 있어야 함.

#         n = len(s)
#         counter = Counter(s)

#         for i in range(n):
#             if s[i] == "0" and target[i] == "1":
#                 if counter["1"] >= 1:
#                     counter["0"] -= 1
#                     counter["1"] += 1
#                 else:
#                     return False

#             if s[i] == "1" and target[i] == "0":
#                 if counter["1"] > 1: # except index i
#                     counter["0"] += 1
#                     counter["1"] -= 1
#                 else:
#                     return False
                
#         return True
