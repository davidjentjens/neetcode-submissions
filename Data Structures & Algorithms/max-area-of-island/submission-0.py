class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        grid_height, grid_width = len(grid), len(grid[0])

        def isWater(pos):
            return grid[pos[0]][pos[1]] == 0

        def getValidNeighbors(start_pos):
            valid_neighbors = []
            i, j = start_pos
            for pos in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width and not isWater(pos):
                    valid_neighbors.append(pos)
            return valid_neighbors

        current_island_area = 0
        max_island_area = 0
        visited = set()
        def dfs(pos):
            nonlocal current_island_area
            if pos in visited:
                return
            visited.add(pos)
            current_island_area += 1
            for neighbor in getValidNeighbors(pos):
                dfs(neighbor)

        for i in range(grid_height):
            for j in range(grid_width):
                pos = (i,j)
                if pos not in visited and not isWater(pos):
                    current_island_area = 0
                    dfs(pos)
                    max_island_area = max(max_island_area, current_island_area)

        return max_island_area
