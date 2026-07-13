from collections import deque

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        grid_height, grid_width = len(maze), len(maze[0])
        DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

        dist = [[float('inf')] * grid_width for _ in range(grid_height)]
        dist[start[0]][start[1]] = 0
        
        queue = deque([(start[0], start[1])])

        # Helper func to determine if the ball has hit a wall node
        # AKA their rolling direction states that the next cell is a wall
        def isRolling(r, c, direction):
            next_r, next_c = r + direction[0], c + direction[1]
            return 0 <= next_r < grid_height and 0 <= next_c < grid_width and maze[next_r][next_c] == 0

        while queue:
            # Pop the cell from the queue
            start_r, start_c = queue.popleft()

            # Roll to each possible direction until we hit a wall, then, only if distance is smaller,
            # log relaxed distance and append up-to-the-wall cell to the queue
            for dr, dc in DIRS:
                r, c = start_r, start_c
                distance = dist[r][c]
                while isRolling(r, c, (dr, dc)):
                    r += dr; c += dc; distance += 1
                if distance < dist[r][c]:
                    dist[r][c] = distance
                    queue.append((r,c))

        final_distance = dist[destination[0]][destination[1]]
        return final_distance if final_distance != float('inf') else -1




