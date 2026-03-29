from bisect import bisect_right

def solution(arr, l, r):
    l -= 1
    r -= 1
    w = r - l + 1

    # 각 블록의 시작 위치
    points = []
    s = 0
    for v in arr:
        points.append(s)
        s += v
    total_len = s

    # prefix[i] = 앞에서 i개 블록까지의 전체 합
    # 각 블록 i의 합은 arr[i] * arr[i]
    prefix = [0]
    for v in arr:
        prefix.append(prefix[-1] + v * v)

    def pref_sum(pos):
        """확장 수열의 [0..pos] 합"""
        if pos < 0:
            return 0
        idx = bisect_right(points, pos) - 1
        return prefix[idx] + arr[idx] * (pos - points[idx] + 1)

    def range_sum(left, right):
        return pref_sum(right) - pref_sum(left - 1)

    def value_at(pos):
        idx = bisect_right(points, pos) - 1
        return arr[idx]

    # 목표 합
    K = range_sum(l, r)

    # 가능한 시작점 개수 = 0 .. last_start
    last_start = total_len - w
    if last_start == 0:
        return [K, 1]

    # 변화가 생기는 위치:
    # S(x+1)-S(x) = value_at(x+w) - value_at(x)
    # value_at(x)가 바뀌는 곳: x = points[i]
    # value_at(x+w)가 바뀌는 곳: x = points[i] - w
    changes = set()
    for p in points[1:]:
        if 1 <= p <= last_start:
            changes.add(p)
        q = p - w
        if 1 <= q <= last_start:
            changes.add(q)

    changes = sorted(changes)

    def count_in_ap(start_val, diff, length, target):
        """
        start_val, start_val+diff, ..., start_val+(length-1)*diff
        에서 target의 등장 횟수
        """
        if diff == 0:
            return length if start_val == target else 0

        num = target - start_val
        if num % diff != 0:
            return 0
        t = num // diff
        return 1 if 0 <= t < length else 0

    # S(0)
    cur_x = 0
    cur_sum = range_sum(0, w - 1)
    count = 0

    # 구간별로 처리
    for nx in changes + [last_start]:
        # [cur_x, nx-1] 구간은 등차수열
        seg_len = nx - cur_x
        if seg_len > 0:
            diff = value_at(cur_x + w) - value_at(cur_x)
            count += count_in_ap(cur_sum, diff, seg_len, K)
            cur_sum += diff * seg_len
            cur_x = nx

    # 마지막 점 S(last_start)
    if cur_sum == K:
        count += 1

    return [K, count]
