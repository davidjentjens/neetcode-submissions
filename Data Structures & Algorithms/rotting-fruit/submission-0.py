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
        
        start_positions = []
        banana_count = 0

        for i in range(grid_height):
            for j in range(grid_width):
                cell = grid[i][j]
                if cell == 1 or cell == 2: banana_count += 1
                if cell == 2: start_positions.append((i,j))
        
        minutes = 0
        queue = deque(start_positions)
        visited = set(start_positions)

        while queue:
            queue_size = len(queue)
            found_new = False
            while queue_size != 0:
                node = queue.popleft()
                queue_size -= 1
                for neighbor in getValidNeighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        found_new = True
            # Once you've traversed the direct neighbors of the previous level, increment the minutes
            if found_new: minutes += 1
        return minutes if banana_count == len(visited) else -1            