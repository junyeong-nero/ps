class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.d = dict()
        self.times = times

        counter = Counter()
        most_voted = 0

        for time, person in sorted(zip(times, persons)):
            counter[person] += 1
            if counter.get(most_voted, 0) <= counter[person]:
                most_voted = person

            self.d[time] = most_voted

        # print(self.d)


    def q(self, t: int) -> int:
        i = bisect_left(self.times, t)
        if not (i < len(self.times) and self.times[i] == t):
            i -= 1
        return self.d[self.times[i]]

