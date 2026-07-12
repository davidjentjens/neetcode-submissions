from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        grid_height, grid_width = len(grid), len(grid[0])
        def getValidNeighbors(start_pos):
            i,j = start_pos
            valid_neighbors = []
            for pos in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width:
                    valid_neighbors.append(pos)
            return valid_neighbors

        # First we must change only one of the islands from 1 to 2
        visited = set()
        def flipIsland(pos):
            if pos in visited:
                return
            visited.add(pos)
            grid[pos[0]][pos[1]] = 2
            for neighbor in getValidNeighbors(pos):
                if grid[neighbor[0]][neighbor[1]] == 1:
                    flipIsland(neighbor)

        island_flipped = False
        for i in range(grid_height):
            if island_flipped: break
            for j in range(grid_width):
                if(grid[i][j] == 1):
                    flipIsland((i,j))
                    island_flipped = True
                    break;

        # Now we seed the bfs will all cells from island 1 and 2
        queue1, queue2 = deque(), deque()
        for i in range(grid_height):
            for j in range(grid_width):
                if(grid[i][j] == 1):
                    queue1.append((i,j))
                if(grid[i][j] == 2):
                    queue2.append((i,j))

        # We determine which island is smaller, so it is more efficient to start from
        ORIGIN, TARGET = 0, 0
        origin_queue = deque()
        if len(queue1) > len(queue2):
            origin_queue = queue2
            ORIGIN = 2
            TARGET = 1
        else:
            origin_queue = queue1
            ORIGIN = 1
            TARGET = 2

        # And finally, do a bfs from the island ORIGIN to island TARGET, and see how many levels it takes
        flipped_levels = 0
        while(origin_queue):
            for _ in range(len(origin_queue)):
                node = origin_queue.popleft()
                for neighbor in getValidNeighbors(node):
                    # If we find island TARGET, return the number of levels it took to get here
                    if grid[neighbor[0]][neighbor[1]] == TARGET:
                        return flipped_levels
                    # We only append unvisited 0 neighbors to the origin_queue, ignoring 1 tiles
                    if grid[neighbor[0]][neighbor[1]] == 0:
                        grid[neighbor[0]][neighbor[1]] = ORIGIN
                        origin_queue.append(neighbor)
            flipped_levels += 1;

        return -1