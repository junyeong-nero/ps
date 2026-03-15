class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.values = []
        self.frozen_count = 0
        self.frozen_value = 0
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        normalized = (val - self.add) % self.MOD
        normalized = normalized * pow(self.mul, self.MOD - 2, self.MOD) % self.MOD
        self.values.append(normalized)

    def addAll(self, inc: int) -> None:
        self.frozen_value = (self.frozen_value + inc) % self.MOD
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        if m == 0:
            self.frozen_count += len(self.values)
            self.values = []
            self.frozen_value = 0
            self.mul = 1
            self.add = 0
            return

        self.frozen_value = (self.frozen_value * m) % self.MOD
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        total_length = self.frozen_count + len(self.values)
        if idx >= total_length:
            return -1

        if idx < self.frozen_count:
            return self.frozen_value

        normalized = self.values[idx - self.frozen_count]
        return (normalized * self.mul + self.add) % self.MOD

# class Fancy:

#     def __init__(self):
#         self.arr = []
#         self.operations = []
#         self.timer = 0

#     def append(self, val: int) -> None:
#         self.arr.append((val, self.timer))
         
#     def addAll(self, inc: int) -> None:
#         self.operations.append((0, inc))
#         self.timer += 1

#     def multAll(self, m: int) -> None:
#         self.operations.append((1, m))
#         self.timer += 1
        
#     def getIndex(self, idx: int) -> int:
#         if idx >= len(self.arr):
#             return -1
        
#         MOD = 10 ** 9 + 7
#         res, start_time = self.arr[idx]
#         for op, value in self.operations[start_time:]:
#             if op == 0:
#                 res += value
#             if op == 1:
#                 res *= value

#             res = res % MOD
        
#         return res
