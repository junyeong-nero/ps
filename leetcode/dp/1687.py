# Greedy Approach


class Solution:
    def boxDelivering(
        self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        # one ship. box limits, total weights
        # boxes[i] = ports, weights

        q = deque()
        weight = 0

        n = len(boxes)
        box_index = 0
        box_complete = 0

        ship_position = 0
        ship_movement = 0

        def can_ship(index):
            nonlocal weight
            return (
                len(q) < maxBoxes
                and index < n
                and weight + boxes[index][1] <= maxWeight
            )

        def ship_all_boxes():
            nonlocal box_index, ship_position, ship_movement, weight

            if ship_position != 0:
                ship_movement += 1
            ship_position = 0

            while can_ship(box_index):
                q.append(boxes[box_index])
                weight += boxes[box_index][1]
                box_index += 1

            # print(q)

        def board_at(port):
            nonlocal ship_position, ship_movement, weight, box_complete

            if ship_position != port:
                ship_movement += 1
            ship_position = port

            while q and q[0][0] == port:
                p, w = q.popleft()
                box_complete += 1
                weight -= w

            # print(q)

        # Greedy Approach
        while box_complete < n:
            if len(q) == 0 or (
                box_index < n and q[0][0] == boxes[box_index][0] and can_ship(box_index)
            ):
                ship_all_boxes()
            else:
                board_at(q[0][0])

        # 만약 지금 가야할 포트가 p 이고, 실어야 한 박스가 p 포트에 가야한다면
        # storage 로 돌아와야 하나? 아니면 그냥 갔다 오는게 맞나?
        # p > 0 > p > 0 4번
        # 0 > p > 0 3번? 무조건 먼저 실는게 맞다.

        if ship_position != 0:
            ship_movement += 1

        return ship_movement


### DP Approach + Sliding Queue


class Solution:
    def boxDelivering(
        self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        n = len(boxes)

        # 무게 prefix
        weight_prefix = [0]
        for i in range(n):
            weight_prefix.append(weight_prefix[-1] + boxes[i][1])

        # 포트 변경 횟수 prefix
        port_change_prefix = [0] * (n + 1)
        for i in range(1, n):
            port_change_prefix[i + 1] = port_change_prefix[i] + (
                1 if boxes[i][0] != boxes[i - 1][0] else 0
            )

        def cost(j, i):
            # boxes[j..i] 를 한 번에 배송하는 이동 횟수
            return 2 + (port_change_prefix[i + 1] - port_change_prefix[j + 1])

        def valid(j, i):
            # boxes[j..i] 를 한 번에 실을 수 있는가
            return (
                i - j + 1 <= maxBoxes
                and weight_prefix[i + 1] - weight_prefix[j] <= maxWeight
            )

        # dp[i] = 앞의 i개 박스를 배송 완료하고 창고로 돌아왔을 때 최소 이동 횟수
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            # 마지막 운송이 boxes[j..i-1] 라고 두기
            for j in range(i - 1, -1, -1):
                if i - j > maxBoxes:
                    break
                if weight_prefix[i] - weight_prefix[j] > maxWeight:
                    continue
                dp[i] = min(dp[i], dp[j] + cost(j, i - 1))

        return dp[n]


### DP + Monotone Queue

from collections import deque
from typing import List


class Solution:
    def boxDelivering(
        self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        n = len(boxes)

        # ws[i] = 앞 i개 박스의 무게 합
        ws = [0] * (n + 1)

        # cs[i] = 앞 i개 박스를 보낼 때,
        # 박스들 사이에서 포트가 바뀐 횟수 누적
        cs = [0] * (n + 1)

        for i in range(1, n + 1):
            port, weight = boxes[i - 1]
            ws[i] = ws[i - 1] + weight
            if i > 1:
                cs[i] = cs[i - 1] + (1 if boxes[i - 1][0] != boxes[i - 2][0] else 0)

        # dp[i] = 앞 i개 박스를 배송 완료하고 창고로 돌아왔을 때 최소 이동 횟수
        dp = [0] + [float("inf")] * n

        dq = deque([0])  # 후보 시작점 j 저장

        for i in range(1, n + 1):
            # 현재 i에 대해 유효하지 않은 j 제거
            while dq and (i - dq[0] > maxBoxes or ws[i] - ws[dq[0]] > maxWeight):
                dq.popleft()

            # 최적 후보로 dp[i] 계산
            j = dq[0]
            dp[i] = dp[j] + (cs[i] - cs[j + 1]) + 2

            # 다음 i들을 위해 현재 i를 후보로 넣기 전에
            # value(i) = dp[i] - cs[i+1] 기준으로 정리
            if i < n:
                val_i = dp[i] - cs[i + 1]
                while dq:
                    back = dq[-1]
                    val_back = dp[back] - cs[back + 1]
                    if val_back >= val_i:
                        dq.pop()
                    else:
                        break
                dq.append(i)

        return dp[n]

