class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        grid_height, grid_length = len(grid), len(grid[0])
        def getValidNeighbors(pos):
            i, j = pos
            valid_neighbors = []
            for pos in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_length:
                    valid_neighbors.append(pos)
            return valid_neighbors
        
        visited = set((0,0))
        queue = deque([((0,0),1)])
        while queue:
            pos, distance = queue.popleft()
            if pos[0] == grid_height - 1 and pos[1] == grid_length - 1:
                return distance
            for neighbor in getValidNeighbors(pos):
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == 0:
                    queue.append((neighbor, distance+1))
                    visited.add(neighbor)
                
        return -1
            