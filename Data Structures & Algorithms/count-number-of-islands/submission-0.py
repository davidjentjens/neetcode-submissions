class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_height, grid_width = len(grid), len(grid[0])

        def getValidNeighbors(start_pos):
            i, j = start_pos
            valid_neighbors = []
            for pos in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width:
                    valid_neighbors.append(pos)
            return valid_neighbors

        def dfs(start_index):
            i, j = start_index
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for neighbor in getValidNeighbors((i, j)):
                dfs(neighbor)

        num_islands = 0

        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j] == "1":
                    dfs((i,j))
                    num_islands += 1

        return num_islands