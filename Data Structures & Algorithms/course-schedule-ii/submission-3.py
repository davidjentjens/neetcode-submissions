class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        top_sort = []

        while queue:
            node = queue.popleft()
            top_sort.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)                 

        return top_sort if len(top_sort) == numCourses else []