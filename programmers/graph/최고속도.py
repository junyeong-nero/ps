from bisect import bisect_left
from collections import defaultdict, deque

def solution(cities, roads):
    
    # 1. 도로위 도시 확인.
    # 2. 도로위에 교차하는 지점 확인
    # 3. 도시 -> 도로위에 있는 교차점 or 새로운 도시로 이동.

    m = len(cities)
    n = len(roads)
    
    INF = float("INF")
    
    def is_vertical(road):
        return road[0] == road[2]      
    
    def get_mid(road):
        return (road[0] + road[2]) // 2, (road[1] + road[3]) // 2
    
    def get_pos(road, x, y):
        mid = get_mid(road)
        if x == mid[0]:
            return 1 if road[1] <= y <= road[3] else None
        if y == mid[1]:
            return 1 if road[0] <= x <= road[2] else None
        return None
    
    def on_road(city, road):
        cx, cy = city
        pos = get_pos(road, cx, cy)
        if pos is not None:
            return True, pos
        
        return False, None
                
    def is_intersect(road1, road2):
        if is_vertical(road1) == is_vertical(road2):
            return None
    
        if not is_vertical(road1) and is_vertical(road2):
            road1, road2 = road2, road1
            
        # road1 : v / road2 : h
        if road2[0] <= road1[0] <= road2[2] and road1[1] <= road2[1] <= road1[3]:
            return (road1[0], road2[1])
    
        return None
    
    
    d = defaultdict(list)
    
    for j, road in enumerate(roads):
        mx, my = get_mid(road)
        d[j].append((road[0], road[1], INF))
        d[j].append((mx, my, road[4]))
        d[j].append((road[2], road[3], INF))
        
    
    for i, city in enumerate(cities):
        for j, road in enumerate(roads):
            check, pos = on_road(city, road)
            if check:
                d[j].append((city[0], city[1], INF))
    
    for i in range(n):
        for j in range(i):
            road1, road2 = roads[i], roads[j]
            temp = is_intersect(road1, road2)
            if temp is None: continue
            
            x, y = temp
            pos_1 = get_pos(road1, x, y)
            pos_2 = get_pos(road2, x, y)
            if pos_1 is not None:
                d[i].append((x, y, INF))
            if pos_2 is not None:
                d[j].append((x, y, INF))
            
    
    print(d)
    
    for idx in d.keys():
        d[idx] = sorted(d[idx])
    
    
    coord2road = defaultdict(list)
    for road_idx in d:
        for idx, (x, y, speed_limit) in enumerate(d[road_idx]):
            coord2road[(x, y)].append((road_idx, idx))
    
    print(coord2road)
    
    def bfs(start_city):
        
        sx, sy = start_city
        q = deque([(sx, sy)])
        
        speed = dict()
        speed[(sx, sy)] = INF

        while q:
            
            cx, cy = q.popleft()
            print(cx, cy)
            
            for road_idx, idx in coord2road[(cx, cy)]:
                if idx - 1 >= 0:
                    nx, ny, speed_limit = d[road_idx][idx - 1]
                    new_speed = min(speed[(cx, cy)], speed_limit)
                    if new_speed > speed.get((nx, ny), 0):
                        speed[(nx, ny)] = new_speed
                        q.append((nx, ny))
                    
                if idx + 1 < len(d[road_idx]):
                    nx, ny, speed_limit = d[road_idx][idx + 1]
                    new_speed = min(speed[(cx, cy)], speed_limit)
                    
                    if new_speed > speed.get((nx, ny), 0):
                        speed[(nx, ny)] = new_speed
                        q.append((nx, ny))
            
                        
            print(speed)            
        
                        
    
    bfs(cities[0])
            
    
            
    
