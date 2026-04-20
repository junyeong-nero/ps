class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        def convert(log):
            _id, _type, _time = log.split(":")
            return int(_id), _type, int(_time)

        logs = [convert(log) for log in logs]
        # logs.sort(key=lambda x: x[2])
        # print(logs)

        time = -1
        stack = deque([])
        res = [0] * n
        time = -1

        for log in logs:
            if log[1] == "start":
                if stack:
                    res[stack[-1][0]] += log[2] - time

                stack.append(log)
                time = log[2]

            if log[1] == "end":
                if stack:
                    temp = stack.pop()[2]
                    res[log[0]] += log[2] - time + 1

                time = log[2] + 1

        # print(res)
        return res

