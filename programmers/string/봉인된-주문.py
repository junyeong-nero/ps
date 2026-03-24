def solution(n, bans):
    
    def get_order(s):
        res, base = 0, 1
        for c in s[::-1]:
            res += base * (ord(c) - ord("a") + 1)
            base *= 26
        return res
    
    def get_string(order):
        s = ""
        while order:
            order -= 1
            s += chr(order % 26 + ord("a"))
            order //= 26
        return s[::-1]
    
    bans = sorted([get_order(ban) for ban in bans])    
    for ban in bans:
        if ban <= n:
            n += 1
    
    # print(bans)
    res = get_string(n)
    return res
