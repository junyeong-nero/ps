from collections import deque

def solution(n, cores):
    
    if n <= len(cores):
        return n

    def func(time):
        res = len(cores)
        for core in cores:
            res += time // core
        return res
    
    left, right = 0, max(cores) * n
    while left < right:
        
        mid = (left + right) // 2
        if func(mid) >= n:
            right = mid
        else:
            left = mid + 1
    
    # print(left, func(left - 1), func(left))
    remainder = n - func(left - 1)
    
    answer = 1
    for idx, core in enumerate(cores):
        if left % core == 0:
            remainder -= 1
            if remainder == 0:
                answer = idx + 1
            
    return answer


# TC
# answer : 4

# at 3, 4
#   0 1 2 3 4
# 1 O O O O O
# 2 O X O X O
# 3 O X X O X
# 4 O X X X O
