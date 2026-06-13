class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        grid_height, grid_width = len(isConnected), len(isConnected[0])
        graph = defaultdict(list)
        for i in range(grid_height):
            for j in range(grid_width):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        num_provinces = 0
        for node in graph:
            if node not in visited:
                dfs(node)
                num_provinces += 1

        return num_provinces

