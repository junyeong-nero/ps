def solution(sequence):
    
    prefix = [[0, 0]]
    n = len(sequence)
    
    for i, num in enumerate(sequence):
        a, b = prefix[-1]
        if i % 2 == 0:
            prefix.append([a + num, b])
        else:
            prefix.append([a, b + num])
    
    # print(prefix)
    min_index1, min_index2 = 0, 0
    res = float("-inf")
    for i in range(n + 1):
        
        a, b = prefix[i]
        res = max(
            res, 
            a - b + prefix[min_index2][1] - prefix[min_index2][0], 
            b - a + prefix[min_index1][0] - prefix[min_index1][1], 
        )
        
        if a - b > prefix[min_index1][0] - prefix[min_index1][1]:
            min_index1 = i
        if b - a > prefix[min_index2][1] - prefix[min_index2][0]:
            min_index2 = i
        
        # for j in range(i):
        #     c, d = prefix[j]
        #     p, q = a - c, b - d
        #     # p - q = a - b + (d - c) -> index2
        #     # q - p = b - d - a + c = b - a + (c - d) -> index1
        #     # maximize c - d or d - c
        #     res = max(res, p - q, q - p)

    return res
