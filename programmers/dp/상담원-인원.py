import heapq

def solution(k, n, reqs):
    d = [[] for _ in range(k)]
    for start, time, type_ in reqs:
        d[type_ - 1].append((start, time))

    for i in range(k):
        d[i].sort()

    def simulate(type_idx, mentors):
        heap = [0] * mentors
        heapq.heapify(heap)
        total_wait = 0

        for start, duration in d[type_idx]:
            end_time = heapq.heappop(heap)

            if end_time <= start:
                heapq.heappush(heap, start + duration)
            else:
                total_wait += end_time - start
                heapq.heappush(heap, end_time + duration)

        return total_wait

    max_m = n - k + 1

    wait = [[0] * (max_m + 1) for _ in range(k)]
    for i in range(k):
        for m in range(1, max_m + 1):
            wait[i][m] = simulate(i, m)

    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for i in range(1, k + 1):
        for total in range(1, n + 1):
            for m in range(1, total + 1):
                if m <= max_m and dp[i - 1][total - m] != INF:
                    dp[i][total] = min(dp[i][total], dp[i - 1][total - m] + wait[i - 1][m])

    return dp[k][n]


# def solution(k, n, reqs):
    
#     # simulation
#     d = [[] for i in range(k)]
#     for start, time, type_ in sorted(reqs):
#         d[type_ - 1].append((start, time))
        
#     allocated = [1] * k
    
#     def simulate(type_):
#         num = allocated[type_]
#         stacks = [[0] for _ in range(num)] 
#         waiting_time = 0
        
#         for start, time in d[type_]:
            
#             temp = 0
#             complete = False
            
#             for idx, stack in enumerate(stacks):
#                 if stack[-1] <= start:
#                     stack.append(start + time)
#                     complete = True
#                     break
                    
#                 if stack[-1] < stacks[temp][-1]:
#                     temp = idx
                    
#             if not complete:
#                 waiting_time += (stacks[temp][-1] - start)
#                 stacks[temp].append(stacks[temp][-1] + time)
            
#         return waiting_time
    
#     def func():
        
#         temp = []
#         for i in range(k):
            
#             allocated[i] += 1
#             arr = [simulate(i) for i in range(k)]
#             allocated[i] -= 1
            
#             temp.append(sum(arr))
        
#         value = min(temp)
#         index = temp.index(value)
        
#         allocated[index] += 1
#         return value
    
#     res = 0
#     for _ in range(n - k):
#         res = func()
        
#     return res
