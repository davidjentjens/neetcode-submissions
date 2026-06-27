class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        grid_height, grid_width = len(grid), len(grid[0])

        def isWater(pos):
            return grid[pos[0]][pos[1]] == 0

        def isOutOfBounds(pos):
            return pos[0] < 0 or pos[0] >= grid_height or pos[1] < 0 or pos[1] >= grid_width

        def getNeighbors(start_pos):
            i, j = start_pos
            return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        
        def getValidNeighbors(start_pos):
            valid_neighbors = []
            for pos in getNeighbors(start_pos):
                if not isOutOfBounds(pos) and not isWater(pos):
                    valid_neighbors.append(pos)
            return valid_neighbors

        def countBorders(start_pos):
            borders = 0
            for pos in getNeighbors(start_pos):
                if isOutOfBounds(pos) or isWater(pos):
                    borders += 1
            return borders

        perimeter = 0
        visited = set()
        def dfs(pos):
            nonlocal perimeter
            if pos in visited:
                return
            visited.add(pos)
            perimeter += countBorders(pos)
            for neighbor in getValidNeighbors(pos):
                dfs(neighbor)

        for i in range(grid_height):
            for j in range(grid_width):
                pos = (i,j)
                if pos not in visited and not isWater(pos):
                    dfs(pos)

        return perimeter