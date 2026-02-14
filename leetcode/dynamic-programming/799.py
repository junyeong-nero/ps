class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Calculates how full a specific glass is in a champagne tower.
        """
        # Initialize the top row with the total amount poured
        current_row = [poured]

        # Simulate the flow row by row
        for _ in range(query_row):
            # Create the next row with one more glass than the current row
            next_row = [0.0] * (len(current_row) + 1)
            
            # Iterate through the current row to distribute champagne
            for i, volume in enumerate(current_row):
                # Only process if there is overflow
                if volume > 1:
                    overflow = (volume - 1) / 2.0
                    next_row[i] += overflow
                    next_row[i + 1] += overflow
            
            # Move to the next row
            current_row = next_row

        # The glass cannot hold more than 1 unit
        return min(1.0, current_row[query_glass])
