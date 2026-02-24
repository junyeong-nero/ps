class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        n = len(arr)
        used = [False] * n
        d_start, d_end = dict(), dict()
        # d_start[i] = j
        # d_end[j] = i

        last_step = -1
        size_counter = Counter()

        for step, index in enumerate(arr):

            index = index - 1
            used_left = index - 1 >= 0 and used[index - 1]
            used_right = index + 1 < n and used[index + 1]
                
            if used_left and used_right:
                left_start, left_end = d_end[index - 1], index - 1
                right_start, right_end = index + 1, d_start[index + 1]
                del d_end[index - 1]
                del d_start[index + 1]

                d_start[left_start] = right_end
                d_end[right_end] = left_start

                size_counter[left_end - left_start + 1] -= 1
                size_counter[right_end - right_start + 1] -= 1
                size_counter[right_end - left_start + 1] += 1

            elif used_left:
                left_start, left_end = d_end[index - 1], index - 1
                del d_end[index - 1]
                d_start[left_start] = index
                d_end[index] = left_start

                size_counter[left_end - left_start + 1] -= 1
                size_counter[index - left_start + 1] += 1

            elif used_right:
                right_start, right_end = index + 1, d_start[index + 1]
                del d_start[index + 1]
                d_start[index] = right_end
                d_end[right_end] = index

                size_counter[right_end - right_start + 1] -= 1
                size_counter[right_end - index + 1] += 1

            else:
                d_start[index] = index
                d_end[index] = index

                size_counter[1] += 1

            used[index] = True
            # print(size_counter)
            if size_counter[m] > 0:
                last_step = step + 1
                
        return last_step 
