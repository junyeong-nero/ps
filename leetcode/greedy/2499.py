from collections import Counter


class Solution:
    def minimumTotalCost(self, A, B):
        n = len(A)

        # Step 1: Collect indices where A[i] == B[i]
        conflict_indices = {
            i for i in range(n)
            if A[i] == B[i]
        }

        # If no conflicts, no cost required
        if not conflict_indices:
            return 0

        # Step 2: Count values at conflict positions
        value_count = Counter(A[i] for i in conflict_indices)

        # Find the dominant value among conflicts
        dominant_value = max(value_count, key=value_count.get)

        # Step 3: Determine how many extra indices are required
        dominant_freq = value_count[dominant_value]
        required_extra = max(2 * dominant_freq - len(conflict_indices), 0)

        # Step 4: Add valid indices to break dominance
        for i in range(n):
            if required_extra == 0:
                break

            if (
                i not in conflict_indices and
                A[i] != dominant_value and
                B[i] != dominant_value
            ):
                conflict_indices.add(i)
                required_extra -= 1

        # Step 5: If still unmet requirement, impossible
        if required_extra > 0:
            return -1

        return sum(conflict_indices)
