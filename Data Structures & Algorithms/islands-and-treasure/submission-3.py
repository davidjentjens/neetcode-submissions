class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        grid_height, grid_width = len(grid), len(grid[0])
        def getValidNeighbors(start_pos):
            r, c = start_pos
            valid_neighbors = []
            for pos in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width :
                    valid_neighbors.append(pos)
            return valid_neighbors

        start_positions = []
        for r in range(grid_height):
            for c in range(grid_width):
                if grid[r][c] == 0: start_positions.append((r,c))

        queue = deque(start_positions)
        visited = set(start_positions)
        distance = 0

        while len(queue) > 0:
            distance += 1
            for _ in range(len(queue)):
                pos = queue.popleft()
                for neighbor in getValidNeighbors(pos):
                    r, c = neighbor
                    if neighbor not in visited and grid[r][c] > 0:
                        grid[r][c] = distance
                        visited.add(neighbor)
                        queue.append(neighbor)