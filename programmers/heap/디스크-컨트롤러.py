import heapq

def solution(jobs):
    
    n = len(jobs)
    jobs = sorted(jobs)
    index = 0
    curr = 0
    
    q = []
    arr = []
    
    while index < n or q:
        
        while index < n and jobs[index][0] <= curr:
            heapq.heappush(q, (jobs[index][1], jobs[index][0], index))
            index += 1
            
        # print(curr, q)
        
        if q:
            time, arrival, job_id = heapq.heappop(q)
            curr += time
            arr.append(curr - arrival)
            
        else:
            curr = jobs[index][0]
            
    # print(arr)
    return sum(arr) // len(arr)
