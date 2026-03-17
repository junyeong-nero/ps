from bisect import bisect_left
from collections import defaultdict

def solution(scores):
    
    # check first => 인사고과를 받을 수 있는지?
    # 이거 체크가 제일 힘들어보이는데
    
    # 이후 a + b sorting 으로 ranking 매기면 끝?
    
    n = len(scores)
    scores = sorted(zip(scores, range(n)))
    
    d = defaultdict(list)
    d_ = defaultdict(list)
    for (a, b), index in scores:
        d[a].append(b)
        d_[a].append(index)
    
    renewals = defaultdict(list)
    
    temp = 0
    for key in sorted(d.keys(), reverse=True):
        
        start = bisect_left(d[key], temp)
        for i in range(start, len(d[key])):
            x = key + d[key][i]
            renewals[x].append(d_[key][i])
        
        temp = max(temp, max(d[key]))
        
    # print(renewals)
    
    rank = 1
    for score in sorted(renewals.keys(), reverse=True):
        if 0 in renewals[score]:
            return rank
        rank += len(renewals[score])

    return -1
    
