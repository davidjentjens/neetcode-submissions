class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 1:
            return True

        graph = {}
        for i,j in prerequisites:
            if i not in graph:
                graph[i] = Node(i, set())
            if j not in graph:
                graph[j] = Node(j, set())
            graph[j].children.add(graph[i])
        
        visited = set()


        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            paths = []
            for child in node.children:
                paths.append(dfs(child))
            visited.remove(node)
            return all(paths)
        
        for node in graph.values():
            is_acyclic = dfs(node)
            visited = set()
            if not is_acyclic:
                return False
        return True

        
