class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            a, b = prerequisite
            graph[b].append(a)
        
        can_finish = True
        path = set()
        visited = set()
        def dfs(node: int):
            nonlocal can_finish
            if not can_finish or node in visited:
                return
            if node in path:
                can_finish = False
                return
            path.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            path.remove(node)
            visited.add(node)

        for node in range(numCourses):
            path = set()
            dfs(node)
            if not can_finish:
                return False

        return True
