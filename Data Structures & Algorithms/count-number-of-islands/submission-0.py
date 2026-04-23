class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs recursive method
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(rows, columns):
            if (rows < 0 or columns < 0 or rows >= ROWS or
                columns >= COLS or grid[rows][columns] == "0"
            ):
                return 
            grid[rows][columns] = "0"
            #loop through rows and append to i -> same with columns
            for i, j in directions:
                dfs(rows + i, columns + j)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands

