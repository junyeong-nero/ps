class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        i = 0 
        while i < n:
            # print(stack)
            if s[i] == "(":
                stack.append("(")
                i += 1
            elif s[i] == ")":
                arr = []
                while stack and stack[-1] != "(":
                    arr.append(stack.pop()[::-1])

                stack.pop() # remove "("
                stack.append("".join(arr))
                i += 1
            else:
                j = i
                while j < n and s[j].isalpha():
                    j += 1
                stack.append(s[i:j])
                i = j

        # print(stack)
        return "".join(stack)

