class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(set)

        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        visited = set()
        node_count = 0

        def dfs(node):
            nonlocal node_count
            if node in visited:
                return
            node_count += 1
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(0)

        return node_count == n 