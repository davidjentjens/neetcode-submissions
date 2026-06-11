class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        
        visited = set()
        path_visited = set()
        top_sort = []

        def dfs(node):
            if node in path_visited:
                return False
            if node in visited:
                return True
            path_visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited.add(node)
            top_sort.append(node)
            path_visited.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        top_sort.reverse()
        return top_sort