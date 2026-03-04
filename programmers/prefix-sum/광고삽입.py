import bisect

def time2num(s):
    h, m, sec = map(int, s.split(":"))
    return h * 3600 + m * 60 + sec

def num2time(t):
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    play_num = time2num(play_time)
    adv_num = time2num(adv_time)

    if adv_num >= play_num:
        return "00:00:00"

    # events[t] = delta viewers at time t
    events = {0: 0, play_num: 0}  # 반드시 play_num 포함해서 마지막 구간 닫기

    for log in logs:
        start, end = log.split("-")
        s = time2num(start)
        e = time2num(end)
        events[s] = events.get(s, 0) + 1
        events[e] = events.get(e, 0) - 1

    keys = sorted(events.keys())
    n = len(keys)

    # view[i] = viewers on interval [keys[i], keys[i+1])
    view = [0] * n
    cur = 0
    for i, t in enumerate(keys):
        cur += events[t]
        view[i] = cur

    # area[i] = total viewer-seconds on [0, keys[i])
    area = [0] * n
    for i in range(n - 1):
        area[i + 1] = area[i] + view[i] * (keys[i + 1] - keys[i])

    def A(t):
        """Total viewer-seconds on [0, t). 0 <= t <= play_num"""
        idx = bisect.bisect_right(keys, t) - 1
        # idx in [0, n-1] because keys includes 0 and play_num
        return area[idx] + view[idx] * (t - keys[idx])

    last_start = play_num - adv_num

    # ✅ 후보 시작 시각: event_time, event_time-adv, 0, last_start
    candidates = {0, last_start}
    for t in keys:
        candidates.add(t)
        candidates.add(t - adv_num)

    best = -1
    ans = 0

    for start in candidates:
        if 0 <= start <= last_start:
            val = A(start + adv_num) - A(start)
            if val > best or (val == best and start < ans):
                best = val
                ans = start

    return num2time(ans)
