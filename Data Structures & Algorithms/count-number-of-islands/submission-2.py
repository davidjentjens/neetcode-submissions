class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def getValidNeighbors(start_pos):
            i, j = start_pos
            valid_neighbors = []
            for pos in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == '1':
                    valid_neighbors.append(pos)
            return valid_neighbors

        def dfs(start_index):
            i, j = start_index
            grid[i][j] = "0"
            for neighbor in getValidNeighbors((i, j)):
                dfs(neighbor)

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs((i,j))
                    num_islands += 1

        return num_islands