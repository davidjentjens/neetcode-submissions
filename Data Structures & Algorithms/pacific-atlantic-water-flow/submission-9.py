class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid_height, grid_width = len(heights), len(heights[0])

        def getValidNeighbors(start_pos):
            i, j = start_pos
            valid_neighbors = []
            for pos in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= pos[0] < grid_height and 0 <= pos[1] < grid_width:
                    if heights[pos[0]][pos[1]] >= heights[i][j]:
                        valid_neighbors.append(pos)
            return valid_neighbors

        oceans = {
            "PACIFIC": set(),
            "ATLANTIC": set()
        }

        visited = set()
        def dfs(pos, ocean):
            if pos in visited or pos in oceans[ocean]:
                return
            visited.add(pos)
            oceans[ocean].add(pos)
            for neighbor in getValidNeighbors(pos):
                dfs(neighbor, ocean)
            visited.remove(pos)

        for r in range(grid_height):
            dfs((r,0), "PACIFIC")
            dfs((r,grid_width-1), "ATLANTIC")

        for c in range(grid_width):
            dfs((0,c), "PACIFIC")
            dfs((grid_height-1,c), "ATLANTIC")

        return list(oceans["PACIFIC"] & oceans["ATLANTIC"])
    