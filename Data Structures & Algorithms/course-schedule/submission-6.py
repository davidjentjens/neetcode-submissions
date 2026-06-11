class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 1:
            return True

        graph = {}
        for i,j in prerequisites:
            if i not in graph:
                graph[i] = set()
            if j not in graph:
                graph[j] = set()
            graph[j].add(i)
        
        visited = set()
        acyclic = set()

        def dfs(node):
            if node in visited:
                return False
            if node in acyclic:
                return True
            visited.add(node)
            paths = []
            for child in graph[node]:
                paths.append(dfs(child))
            visited.remove(node)
            all_paths_acyclic = all(paths)
            if all_paths_acyclic:
                acyclic.add(node)
            return all_paths_acyclic
        
        for node in graph:
            if node in acyclic:
                continue
            is_acyclic = dfs(node)
            if not is_acyclic:
                return False
        return True

        
