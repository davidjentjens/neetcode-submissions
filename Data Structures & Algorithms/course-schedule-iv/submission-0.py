class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            a, b = prerequisite
            graph[b].append(a)

        reachability_matrix = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        visited = set()
        def dfs(node, parent_val):
            if node in visited:
                return
            reachability_matrix[parent_val][node] = True
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor, parent_val)

        for node in range(numCourses):
            dfs(node, node)
            visited = set()
        
        res = []
        for query in queries:
            a, b = query
            res.append(reachability_matrix[b][a])

        return res
        