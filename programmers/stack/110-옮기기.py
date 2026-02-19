def solution(s):
    answer = []
    for x in s:
        stack = []
        k = 0

        # 1) remove all "110"
        for ch in x:
            if ch == '0' and len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1':
                stack.pop()
                stack.pop()
                k += 1
            else:
                stack.append(ch)

        rest = ''.join(stack)

        # 2) insert "110"*k at the best position
        insert = "110" * k
        last0 = rest.rfind('0')

        if last0 == -1:
            # no '0' in rest
            answer.append(insert + rest)
        else:
            answer.append(rest[:last0 + 1] + insert + rest[last0 + 1:])

    return answer
