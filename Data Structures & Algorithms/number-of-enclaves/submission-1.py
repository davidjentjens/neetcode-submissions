class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        grid_height, grid_width = len(grid), len(grid[0])
        def isBorder(pos):
            i,j = pos
            return i == 0 or i == grid_height -1 or j == 0 or j == grid_width-1

        start_positions = []
        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j] == 1 and isBorder((i,j)):
                    start_positions.append((i,j))
        
        def getValidNeighbors(start_pos):
            i, j = start_pos
            neighbors = []
            for pos in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width:
                    neighbors.append(pos)
            return neighbors

        def dfs(pos):
            i, j = pos
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            for neighbor in getValidNeighbors(pos):
                dfs(neighbor)

        for pos in start_positions:
            dfs(pos)
        
        land_cells = 0
        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j] == 1:
                    land_cells += 1

        return land_cells
                    