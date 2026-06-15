class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        grid_height, grid_width = len(grid), len(grid[0])
        def getValidNeighbors(start_pos):
            i, j = start_pos
            valid_neighbors = []
            for pos in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width:
                    valid_neighbors.append(pos)
            return valid_neighbors

        start_positions = []
        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j] == 0: start_positions.append((i,j))

        queue = deque(start_positions)
        visited = set(start_positions)
        distance = 0

        while len(queue) > 0:
            n = len(queue)
            distance += 1
            for _ in range(n):
                pos = queue.popleft()
                cell = grid[pos[0]][pos[1]]
                for neighbor in getValidNeighbors(pos):
                    neighbor_cell = grid[neighbor[0]][neighbor[1]]
                    if neighbor not in visited and neighbor_cell > 0:
                        grid[neighbor[0]][neighbor[1]] = min(neighbor_cell, distance)
                        queue.append(neighbor)
                        visited.add(neighbor)