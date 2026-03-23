def solution(expressions):
    
    completes = []
    problems = []
    
    for exp in expressions:
        args = exp.split()
        if args[-1] == "X":
            problems.append(args)
        else:
            completes.append(args)
            
    candidates = set(range(2, 10)) 
    
    def func(args):
        nums = [args[0], args[2], args[4]]
        for num in nums:
            if num == "X":
                continue
            end = int(max(num))
            for base in range(2, end + 1):
                if base in candidates:
                    candidates.remove(base)
    
    def func2(args):
        num1, num2, num3 = args[0], args[2], args[4]
        for base in candidates.copy():
            num1_t = int(num1, base)
            num2_t = int(num2, base)
            num3_t = int(num3, base)
            
            if args[1] == "+" and num1_t + num2_t != num3_t:
                candidates.remove(base)
        
            if args[1] == "-" and num1_t - num2_t != num3_t:
                candidates.remove(base)
    
    
    for args in completes:
        func(args) 
        
    for args in problems:
        func(args) 
    
    for args in completes:
        func2(args) 
        if len(candidates) == 1:
            break
    
    
    # print(candidates)
    
    def convert(num, base):
        if num == 0:
            return "0"
        arr = []
        while num:
            arr.append(str(num % base))
            num //= base
        return "".join(arr[::-1])
    
    def func3(args):
        num1, num2, num3 = args[0], args[2], args[4]
        
        d = set()
        for base in candidates.copy():
            num1_t = int(num1, base)
            num2_t = int(num2, base)
            
            if args[1] == "+":
                d.add(convert(num1_t + num2_t, base))
        
            if args[1] == "-":
                d.add(convert(num1_t - num2_t, base))
        
        args.pop()
        if len(d) == 1:
            args.append(next(iter(d)))
        else:
            args.append("?")
        
        return " ".join(args)
    
    
    res = []
    for args in problems:
        res.append(func3(args))
    
    return res
