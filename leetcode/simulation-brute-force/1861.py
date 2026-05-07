class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        m, n = len(boxGrid), len(boxGrid[0])
        
        def rotate_row(arr):
            res = []
            stone, empty = 0, 0
            for i in range(n):
                if arr[i] == "*":
                    res += ["."] * empty
                    res += ["#"] * stone
                    res.append("*")
                    stone, empty = 0, 0

                if arr[i] == "#":
                    stone += 1
                if arr[i] == ".":
                    empty += 1

            res += ["."] * empty
            res += ["#"] * stone
            return res

        grid = []
        for row in boxGrid:
            grid.append(rotate_row(row))
            
        grid = grid[::-1]

        res = []
        for column in zip(*grid):
            res.append(list(column))
        
        return res

