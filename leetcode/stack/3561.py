class Solution:
    def resultingString(self, s: str) -> str:

        def charAdjacency(s1: str, s2: str) -> bool:
            if abs(ord(s1) - ord(s2)) == 1:
                return True
            elif  set([s1, s2]) == set(["a", "z"]):
                return True
            return False

        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            elif charAdjacency(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


# class Solution:
#     def resultingString(self, s: str) -> str:
#         q = deque(list(s))

#         def is_adjacent(a, b):
#             if a == "a" and b == "z" or a == "z" and b == "a":
#                 return True
#             return abs(ord(a) - ord(b)) == 1
        
#         def query(right):
#             left = deque() 
#             changed = False
#             while right:
#                 tar = right.popleft()
#                 left.append(tar)

#                 while left and right and is_adjacent(left[-1], right[0]):
#                     changed = True
#                     left.pop()
#                     right.popleft()

#             return left, changed

#         # abcdefghijklmnopqrs
        
#         while True:
#             q, changed = query(q)
#             if not changed:
#                 break
#             # print(q)

#         # print(q)
#         return "".join(q)
            

                

