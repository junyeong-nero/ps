from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ones = sum(arr)

        if ones % 3 != 0:
            return [-1, -1]

        if ones == 0:
            return [0, n - 1]

        k = ones // 3

        first = second = third = -1
        count = 0

        for i, num in enumerate(arr):
            if num == 1:
                count += 1

                if count == 1:
                    first = i
                elif count == k + 1:
                    second = i
                elif count == 2 * k + 1:
                    third = i

        length = n - third

        # 앞의 두 파트가 세 번째 파트만큼의 길이를 확보할 수 없는 경우
        if first + length > second:
            return [-1, -1]

        if second + length > third:
            return [-1, -1]

        part1 = arr[first:first + length]
        part2 = arr[second:second + length]
        part3 = arr[third:]

        if part1 == part2 == part3:
            return [first + length - 1, second + length]

        return [-1, -1]
