def solution(s):
    
    n = len(s)
    
    def check(index):
        
        temp = 0
        
        i = index + 1
        j = index
        while i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
            i -= 1
            j += 1
        
        if 0 <= i < n and 0 <= j < n:
            temp = max(temp, j - i + 1)
        
        i = index
        j = index
        while i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
            i -= 1
            j += 1
        
        if 0 <= i < n and 0 <= j < n:
            temp = max(temp, j - i + 1)
            
        return temp
        
    res = 0
    for i in range(n):
        res = max(res, check(i))
    
    return res
