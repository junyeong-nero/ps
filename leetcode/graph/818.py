class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        res = 0


        complete = False
        visited = set()

        while q and not complete:

            # print(q)
            res += 1

            for _ in range(len(q)):
                pos, speed = q.popleft()

                if (pos, speed) in visited:
                    continue
                    
                visited.add((pos, speed))

                if (pos == target):
                    complete = True
                    break
                
                A = (pos + speed, speed * 2)
                R = (pos, -1 if speed > 0 else 1)
                if A not in visited: q.append(A)
                if R not in visited: q.append(R)

        return res - 1
            
