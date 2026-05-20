class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    
        n = len(status)

        # problem:
        # keys[i] = list of boxes that can open after opening i-th box
        # contained box = list of box after opening i-th box

        # design:
        # 전형적인 BFS 스타일 완전탐색?
        # 시작 box 나오고, 거기서 얻을 수 있는 keys + 열 수 있는 boxes 확인하면 될듯
        # 순서가 중요할 것 같은데. 예를 들면, 하나의 경로로 갔다가 다시 방문할 수 도 있음.
        # 방문한 box 들 중에서 잠긴 박스들만 유지하면 될 것 같다.
        # 그리고 새롭게 방문한 box 로 key 를 얻으면 잠긴 박스들 위주로 탐색
        
        # time complexity
        # 모든 박스들 방문함.

        # space complexity
        # - 방문한 결국 잠긴 박스들 유지할거기 때문에 n 을 넘기지 않음.


        q = deque(initialBoxes)
        res = 0

        while q: 

            changed = 0
            for i in range(len(q)):
                
                cur = q.popleft()
                if status[cur] == 0:
                    q.append(cur)
                    continue
                else:
                    changed += 1    
                    res += candies[cur]
                    for elem in keys[cur]: status[elem] = 1
                    for elem in containedBoxes[cur]: q.append(elem)
            
            if changed == 0:
                break
        
        return res
