import math

def solution(n, stations, w):

    # 커버하지 못하는 구역의 길이를 확인 -> 길이를 2w + 1 으로 나누면 될듯?
    
    prefix = dict()
    for station in stations:
        prefix[station - w] = prefix.get(station - w, 0) + 1
        prefix[station + w + 1] = prefix.get(station + w + 1, 0) - 1
        
    hist = []
    prev = 1
    curr = 0
    for pos in sorted(prefix.keys()):
        if curr == 0:
            hist.append((prev, pos))        
        
        prev = pos
        curr += prefix[pos]

    if prev < n + 1:
        hist.append((prev, n + 1))
        
    res = 0
    for a, b in hist:
        res += math.ceil((b - a) / (2 * w + 1))

    return res
