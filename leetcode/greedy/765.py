class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2

        # 일단 잘못 앉은 커플이 얼마나 있는지 확인을 해야 함.
        # (i, j) -> 이놈들이 잘못 앉은 경우에 두 가지 방법이 있다.
        # i 를 옮기거나, j 를 옮기거나 -> 골치아프구만.
        # graph + cycle check 형식으로 가야하나?

        # (0, 2) / (1, 3)
        # couple index : c-index
        # 0 -> 1 or 1 -> 0 / 1 -> 0 or 0 -> 1
        # 양방향으로 요청한다면 주저없이 교체를 해버리면 된다.

        # (0, 2) / (1, 5) / (3, 4)
        # (0, 2) : (0 -> 1) / (1 -> 0)
        # (1, 5) : (0 -> 2) / (2 -> 0)
        # (3, 4) : (1 -> 2) / (2 -> 1)
        # 이런 경우에는 2번 해야된다.

        # 근데 이런 경우에 cylic check 로 푸는게 아니었던 것 같은데.

        count = 0

        for i in range(n):
            a, b = row[2 * i], row[2 * i + 1]
            if a > b:
                a, b = b, a
            
            # 일단 작은 녀석이 항상 짝수여야 하고 + 1 더하면 커플이여야 함
            if a & 0 == 1 or a + 1 != b:
                count += 1
        
        print(count)
        if count == 0:
            return 0
        
        return -1


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: i for i, person in enumerate(row)}
        ans = 0

        for i in range(0, len(row), 2):
            x = row[i]
            partner = x ^ 1

            if row[i + 1] == partner:
                continue

            partner_idx = pos[partner]

            # row[i+1] 와 partner를 swap
            row[i + 1], row[partner_idx] = row[partner_idx], row[i + 1]

            # 위치 정보 갱신
            pos[row[partner_idx]] = partner_idx
            pos[row[i + 1]] = i + 1

            ans += 1

        return ans
