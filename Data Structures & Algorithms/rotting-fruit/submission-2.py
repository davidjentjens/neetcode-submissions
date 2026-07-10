from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        grid_height, grid_width = len(grid), len(grid[0])

        def getValidNeighbors(start_pos):
            i, j = start_pos
            valid_neighbors = []
            for pos in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width and grid[pos[0]][pos[1]] == 1:
                    valid_neighbors.append(pos)
            return valid_neighbors

        queue = deque()

        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j] == 2:
                    queue.append((i,j))

        minutes = 0

        while queue:
            rotted_orange = False
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in getValidNeighbors(node):
                    rotted_orange = True
                    grid[neighbor[0]][neighbor[1]] = 2
                    queue.append(neighbor)
            if rotted_orange: minutes += 1

        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j] == 1:
                    return -1

        return minutes