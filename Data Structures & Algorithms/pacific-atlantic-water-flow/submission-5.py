class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        heights_height, heights_width = len(heights), len(heights[0])
        def getValidNeighbors(start_pos):
            i, j = start_pos
            start_height = heights[i][j]
            valid_neighbors = []
            for pos in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= pos[0] < heights_height and 0 <= pos[1] < heights_width:
                    height = heights[pos[0]][pos[1]]
                    if height >= start_height:
                        valid_neighbors.append(pos)
            return valid_neighbors
        
        visited = set()
        found_ocean_global = {
            "PACIFIC": set(),
            "ATLANTIC": set()
        }

        def flow(pos, ocean):
            if pos in visited or pos in found_ocean_global[ocean]:
                return

            found_ocean_global[ocean].add(pos)
            visited.add(pos)

            for neighbor in getValidNeighbors(pos):
                flow(neighbor, ocean)
            
            visited.remove(pos)

        for i in range(heights_height):
            flow((i,0), 'PACIFIC')
            flow((i,heights_width-1), 'ATLANTIC')
        for j in range(heights_width):
            flow((0,j), 'PACIFIC')
            flow((heights_height-1,j), 'ATLANTIC')

        return list(found_ocean_global['PACIFIC'] & found_ocean_global['ATLANTIC'])
            
        